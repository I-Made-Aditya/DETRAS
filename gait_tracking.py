from dataclasses import dataclass
from matplotlib import animation
from scipy.interpolate import interp1d
from PySide6.QtWidgets import QWidget, QVBoxLayout, QApplication
import imufusion
import matplotlib.pyplot as pyplot
import numpy

class Trajectory(QWidget):
    def __init__(self, imu_data=None, parent=None):
        super().__init__(parent)
        self.imu_data = imu_data
        self.initUI()

    def initUI(self):
        self.figure = pyplot.figure(figsize=(2.5, 2.5))
        self.canvas = self.figure.canvas
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

        self.timestamp = None
        self.gyroscope = None
        self.accelerometer = None
        self.sample_rate = 400

        if self.imu_data is not None:
            self.load_data(self.imu_data)

        self.process_data()
        self.create_animation()

    def load_data(self, imu_data):
        self.timestamp = numpy.arange(len(imu_data["timestamps"]))
        self.accelerometer = numpy.column_stack((imu_data["accel_x"], imu_data["accel_y"], imu_data["accel_z"]))
        self.gyroscope = numpy.column_stack((imu_data["gyro_x"], imu_data["gyro_y"], imu_data["gyro_z"]))

    def process_data(self):
        sample_rate = self.sample_rate
        timestamp = self.timestamp
        accelerometer = self.accelerometer
        gyroscope = self.gyroscope
        
        offset = imufusion.Offset(sample_rate)
        ahrs = imufusion.Ahrs()

        ahrs.settings = imufusion.Settings(imufusion.CONVENTION_NWU,
                                           0.5,  # gain
                                           2000,  # gyroscope range
                                           10,  # acceleration rejection
                                           0,  # magnetic rejection
                                           5 * sample_rate)  # rejection timeout = 5 seconds

        delta_time = numpy.diff(timestamp, prepend=timestamp[0])
        euler = numpy.empty((len(timestamp), 3))
        internal_states = numpy.empty((len(timestamp), 3))
        acceleration = numpy.empty((len(timestamp), 3))

        for index in range(len(timestamp)):
            gyroscope[index] = offset.update(gyroscope[index])
            ahrs.update_no_magnetometer(gyroscope[index], accelerometer[index], delta_time[index])
            euler[index] = ahrs.quaternion.to_euler()

            ahrs_internal_states = ahrs.internal_states
            internal_states[index] = numpy.array([ahrs_internal_states.acceleration_error,
                                                  ahrs_internal_states.accelerometer_ignored,
                                                  ahrs_internal_states.acceleration_recovery_trigger])
            acceleration[index] = 9.81 * ahrs.earth_acceleration  # convert g to m/s/s

        is_moving = numpy.empty(len(timestamp))
        for index in range(len(timestamp)):
            is_moving[index] = numpy.sqrt(acceleration[index].dot(acceleration[index])) > 3  # threshold = 3 m/s/s

        margin = int(0.1 * sample_rate)  # 100 ms
        for index in range(len(timestamp) - margin):
            is_moving[index] = any(is_moving[index:(index + margin)])  # add leading margin
        for index in range(len(timestamp) - 1, margin, -1):
            is_moving[index] = any(is_moving[(index - margin):index])  # add trailing margin

        velocity = numpy.zeros((len(timestamp), 3))
        for index in range(len(timestamp)):
            if is_moving[index]:  # only integrate if moving
                velocity[index] = velocity[index - 1] + delta_time[index] * acceleration[index]

        is_moving_diff = numpy.diff(is_moving, append=is_moving[-1])

        @dataclass
        class IsMovingPeriod:
            start_index: int = -1
            stop_index: int = -1

        is_moving_periods = []
        is_moving_period = IsMovingPeriod()

        for index in range(len(timestamp)):
            if is_moving_period.start_index == -1:
                if is_moving_diff[index] == 1:
                    is_moving_period.start_index = index

            elif is_moving_period.stop_index == -1:
                if is_moving_diff[index] == -1:
                    is_moving_period.stop_index = index
                    is_moving_periods.append(is_moving_period)
                    is_moving_period = IsMovingPeriod()

        velocity_drift = numpy.zeros((len(timestamp), 3))

        for is_moving_period in is_moving_periods:
            start_index = is_moving_period.start_index
            stop_index = is_moving_period.stop_index

            t = [timestamp[start_index], timestamp[stop_index]]
            x = [velocity[start_index, 0], velocity[stop_index, 0]]
            y = [velocity[start_index, 1], velocity[stop_index, 1]]
            z = [velocity[start_index, 2], velocity[stop_index, 2]]

            t_new = timestamp[start_index:(stop_index + 1)]

            velocity_drift[start_index:(stop_index + 1), 0] = interp1d(t, x)(t_new)
            velocity_drift[start_index:(stop_index + 1), 1] = interp1d(t, y)(t_new)
            velocity_drift[start_index:(stop_index + 1), 2] = interp1d(t, z)(t_new)

        velocity = velocity - velocity_drift

        position = numpy.zeros((len(timestamp), 3))
        for index in range(len(timestamp)):
            position[index] = position[index - 1] + delta_time[index] * velocity[index]

        self.position = position

    def create_animation(self):
        timestamp = self.timestamp
        position = self.position
        sample_rate = self.sample_rate

        axes = self.figure.add_subplot(111, projection='3d')
        axes.set_xlabel("m")
        axes.set_ylabel("m")
        axes.set_zlabel("m")

        x = []
        y = []
        z = []

        scatter = axes.scatter(x, y, z)

        fps = 30

        def update(frame):
            time_increment = timestamp[frame + 1] - timestamp[frame] if frame < len(timestamp) - 1 else 0

            axes.set_title("{:.3f}".format(timestamp[frame]) + " s")

            x.append(position[frame, 0])
            y.append(position[frame, 1])
            z.append(position[frame, 2])

            scatter._offsets3d = (x, y, z)

            if (min(x) != max(x)) and (min(y) != max(y)) and (min(z) != max(z)):
                axes.set_xlim3d(min(x), max(x))
                axes.set_ylim3d(min(y), max(y))
                axes.set_zlim3d(min(z), max(z))

                axes.set_box_aspect((numpy.ptp(x), numpy.ptp(y), numpy.ptp(z)))

            return scatter

        self.anim = animation.FuncAnimation(self.figure, update,
                                            frames=len(timestamp) - 1,
                                            interval=1000 / fps,
                                            repeat=False)

    def start_animation(self):
        self.anim.event_source.start()

    def stop_animation(self):
        self.anim.event_source.stop()

# if __name__ == "__main__":
#     app = QApplication([])
#     window = Trajectory()
#     window.show()
#     app.exec()
