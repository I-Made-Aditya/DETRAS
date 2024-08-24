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
    def __init__(self, parent=None):
        super().__init__(parent)
        format = QSurfaceFormat()
        format.setVersion(4, 6)
        format.setProfile(QSurfaceFormat.CoreProfile)
        QSurfaceFormat.setDefaultFormat(format)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(60)  # Set to 16 ms for approximately 60 FPS

        # Load data from CSV
        self.data = pd.read_csv('Data_Sample/euler_data.csv')
        self.data_index = 0
        self.start_time = time.time()

        # Initial rotation angles
        self.yaw = 0.0
        self.pitch = 0.0
        self.roll = 0.0

        # Shader program and uniforms
        self.shader_program = None
        self.model_loc = None
        self.proj_loc = None
        self.view_loc = None

        # Model data
        self.indices = None
        self.obj_data = None
        self.texture = None

    def initializeGL(self):
        # Setup OpenGL settings
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        # Compile and link shaders
        self.shader_program = compileProgram(
            compileShader(vertex_src, GL_VERTEX_SHADER),
            compileShader(fragment_src, GL_FRAGMENT_SHADER)
        )
        glUseProgram(self.shader_program)

        # Load model data
        self.indices, self.obj_data = ObjLoader.load_model("Car.obj")

        # Generate and bind VBO
        buffer = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, buffer)
        glBufferData(GL_ARRAY_BUFFER, self.obj_data.nbytes, self.obj_data, GL_STATIC_DRAW)

        # Generate and bind EBO
        ibuffer = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ibuffer)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, self.indices.nbytes, self.indices, GL_STATIC_DRAW)

        # Generate and bind texture
        self.texture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, self.texture)

        # Set texture parameters
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

        # Load texture image
        image = Image.open("car.png")
        image = image.transpose(Image.FLIP_TOP_BOTTOM)
        image_data = image.convert("RGBA").tobytes()
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.width, image.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data)

        # Enable vertex attributes
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(0))

        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(12))

        # Get uniform locations
        self.model_loc = glGetUniformLocation(self.shader_program, "model")
        self.proj_loc = glGetUniformLocation(self.shader_program, "projection")
        self.view_loc = glGetUniformLocation(self.shader_program, "view")

        # Set clear color to white
        glClearColor(1.0, 1.0, 1.0, 1.0)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glUseProgram(self.shader_program)

        # Update rotation angles based on CSV input
        self.update_rotation()

        # Create rotation matrices
        rotx = pyrr.Matrix44.from_x_rotation(np.radians(self.pitch))
        roty = pyrr.Matrix44.from_y_rotation(np.radians(self.yaw))
        rotz = pyrr.Matrix44.from_z_rotation(np.radians(self.roll))
        rot_mat = roty * rotx * rotz
        model_mat = pyrr.matrix44.multiply(rot_mat, pyrr.matrix44.create_from_translation(pyrr.Vector3([0, 0, 0])))

        # Set transformation matrices in shader
        glUniformMatrix4fv(self.model_loc, 1, GL_FALSE, model_mat)
        glUniformMatrix4fv(self.proj_loc, 1, GL_FALSE, pyrr.matrix44.create_perspective_projection_matrix(45, self.width() / self.height(), 0.1, 100))
        glUniformMatrix4fv(self.view_loc, 1, GL_FALSE, pyrr.matrix44.create_look_at(pyrr.Vector3([-5, 1.5, 0]), pyrr.Vector3([0, 0, 0]), pyrr.Vector3([0, 1, 0])))

        # Bind texture
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, self.texture)
        glUniform1i(glGetUniformLocation(self.shader_program, "s_tex"), 0)
        
        # Draw the object
        glDrawElements(GL_TRIANGLES, len(self.indices), GL_UNSIGNED_INT, None)

    def update_rotation(self):
        current_time = time.time()
        elapsed_time = current_time - self.start_time

        if self.data_index < len(self.data):
            timestamp = self.data.loc[self.data_index, 'timestamp']
            if elapsed_time >= timestamp:
                self.roll = self.data.loc[self.data_index, 'roll']
                self.pitch = self.data.loc[self.data_index, 'pitch']
                self.yaw = self.data.loc[self.data_index, 'yaw']
                print(f"Updating rotation: timestamp={timestamp}, roll={self.roll}, pitch={self.pitch}, yaw={self.yaw}")
                self.data_index += 1
            else:
                print(f"Waiting for timestamp={timestamp}, elapsed_time={elapsed_time}")

if __name__ == "__main__":
    app = QApplication([])
    window = OpenGLWidget()
    window.show()
    app.exec()
