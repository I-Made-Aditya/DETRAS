import os
import time
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from OpenGL.GL import *
from OpenGL.GL.shaders import compileShader, compileProgram
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PySide6.QtOpenGLWidgets import *
import numpy as np
import pyrr
import pandas as pd
from PIL import Image
from obj_loader import ObjLoader

# Vertex shader source code
vertex_src = """
#version 330
layout(location=0) in vec3 v_pos;
layout(location=1) in vec2 texture;
uniform mat4 model;
uniform mat4 projection;
uniform mat4 view;
out vec2 v_tex;
void main()
{
    gl_Position = projection * view * model * vec4(v_pos, 1.0);
    v_tex = texture;
}
"""

# Fragment shader source code
fragment_src = """
#version 330
out vec4 out_color;
in vec2 v_tex;
uniform sampler2D s_tex;
void main()
{
    out_color = texture(s_tex, v_tex);
}
"""

class OpenGLWidget(QOpenGLWidget):
    def __init__(self, euler_data=None, parent=None):
        super().__init__(parent)
        format = QSurfaceFormat()
        format.setVersion(4, 6)
        format.setProfile(QSurfaceFormat.CoreProfile)
        QSurfaceFormat.setDefaultFormat(format)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(16)  # Set to 16 ms for approximately 60 FPS

        self.data = pd.DataFrame(euler_data)
        self.data_index = 0
        self.start_time = time.time()

        self.yaw = 0.0
        self.pitch = 0.0
        self.roll = 0.0

        self.prev_timestamp = 0.0

        self.shader_program = None
        self.model_loc = None
        self.proj_loc = None
        self.view_loc = None

        self.indices = None
        self.obj_data = None
        self.texture = None

        self.vbo = None
        self.vao = None

    def initializeGL(self):
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        self.shader_program = self.initShaders()
        self.vbo, self.vao, self.indices = self.initBuffers()
        self.initTextures()

        self.model_loc = glGetUniformLocation(self.shader_program, "model")
        self.proj_loc = glGetUniformLocation(self.shader_program, "projection")
        self.view_loc = glGetUniformLocation(self.shader_program, "view")

        glClearColor(1.0, 1.0, 1.0, 1.0)

    def initShaders(self):
        return compileProgram(
            compileShader(vertex_src, GL_VERTEX_SHADER),
            compileShader(fragment_src, GL_FRAGMENT_SHADER)
        )

    def initBuffers(self):
        indices, obj_data = ObjLoader.load_model("Car.obj")

        vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, vbo)
        glBufferData(GL_ARRAY_BUFFER, obj_data.nbytes, obj_data, GL_STATIC_DRAW)

        vao = glGenVertexArrays(1)
        glBindVertexArray(vao)

        ibuffer = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ibuffer)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.nbytes, indices, GL_STATIC_DRAW)

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(0))

        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(12))

        return vbo, vao, indices

    def initTextures(self):
        self.texture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, self.texture)

        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

        image = Image.open("car.png")
        image = image.transpose(Image.FLIP_TOP_BOTTOM)
        image_data = image.convert("RGBA").tobytes()
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.width, image.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glUseProgram(self.shader_program)

        self.update_rotation()

        rotx = pyrr.Matrix44.from_x_rotation(np.radians(self.pitch))
        roty = pyrr.Matrix44.from_y_rotation(np.radians(self.yaw))
        rotz = pyrr.Matrix44.from_z_rotation(np.radians(self.roll))
        rot_mat = roty * rotx * rotz
        model_mat = pyrr.matrix44.multiply(rot_mat, pyrr.matrix44.create_from_translation(pyrr.Vector3([0, 0, 0])))

        glUniformMatrix4fv(self.model_loc, 1, GL_FALSE, model_mat)
        glUniformMatrix4fv(self.proj_loc, 1, GL_FALSE, pyrr.matrix44.create_perspective_projection_matrix(45, self.width() / self.height(), 0.1, 100))
        glUniformMatrix4fv(self.view_loc, 1, GL_FALSE, pyrr.matrix44.create_look_at(pyrr.Vector3([-5, 1.5, 0]), pyrr.Vector3([0, 0, 0]), pyrr.Vector3([0, 1, 0])))

        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, self.texture)
        glUniform1i(glGetUniformLocation(self.shader_program, "s_tex"), 0)

        glBindVertexArray(self.vao)
        glDrawElements(GL_TRIANGLES, len(self.indices), GL_UNSIGNED_INT, None)

    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)

    def update_rotation(self):
        current_time = time.time()
        elapsed_time = current_time - self.start_time

        if self.data_index < len(self.data):
            timestamp = self.data.loc[self.data_index, 'timestamp']
            delta_time = timestamp - self.prev_timestamp

            if delta_time > 0:
                self.roll = self.data.loc[self.data_index, 'roll']
                self.pitch = self.data.loc[self.data_index, 'pitch']
                self.yaw = self.data.loc[self.data_index, 'yaw']
                self.data_index += 1
                self.prev_timestamp = timestamp

    def stopRendering(self):
        self.timer.stop()

    def cleanup(self):
        self.makeCurrent()
        glDeleteProgram(self.shader_program)
        glDeleteBuffers(1, [self.vbo])
        glDeleteVertexArrays(1, [self.vao])
        glDeleteTextures(1, [self.texture])
        self.doneCurrent()



# if __name__ == "__main__":
#     app = QApplication([])
#     window = OpenGLWidget()
#     window.show()
#     app.exec()
