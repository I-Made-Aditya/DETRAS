import numpy as np
import pandas as pd
from scipy.spatial.transform import Rotation as R
import math

class Connection:
    def __init__(self):
        self.quaternion_file = None
        self.euler_file = None
    
    def convert_to_quaternion(self, imu_data, dt):
        # Extracting accel and gyro data from imu_data dictionary
        accel_data = np.column_stack((imu_data['acc_x'], imu_data['acc_y'], imu_data['acc_z']))
        gyro_data = np.column_stack((imu_data['gyro_x'], imu_data['gyro_y'], imu_data['gyro_z']))
        
        # The length of the data
        n = len(imu_data['timestamps'])
        quaternions = np.zeros((n, 4))
        quaternions[0] = [1, 0, 0, 0]  # initial quaternion

        for i in range(1, n):
            omega = gyro_data[i] * dt
            rotation = R.from_rotvec(omega)
            q_prev = R.from_quat(quaternions[i - 1])
            q_new = q_prev * rotation
            quaternions[i] = q_new.as_quat()

            # Correcting using accelerometer data to prevent drift
            g_accel = accel_data[i] / np.linalg.norm(accel_data[i])
            g_est = q_new.apply([0, 0, 1])
            error = np.cross(g_est, g_accel)
            correction = R.from_rotvec(0.1 * error)
            q_new_corrected = q_new * correction
            quaternions[i] = q_new_corrected.as_quat()

        return quaternions
    
    def convert_to_euler(self, imu_data, dt):
        accel_data = np.column_stack((imu_data['acc_x'], imu_data['acc_y'], imu_data['acc_z']))
        gyro_data = np.column_stack((imu_data['gyro_x'], imu_data['gyro_y'], imu_data['gyro_z']))
        
        # The length of the data
        n = len(imu_data['timestamps'])
        gyro_angles = [0.0, 0.0, 0.0]
        euler_angles_list = []

        for i in range(n):
            ax, ay, az = accel_data[i]
            gx, gy, gz = gyro_data[i]

            # Calculate angles from accelerometer
            roll_acc = np.arctan2(ay, az) * 180 / np.pi
            pitch_acc = np.arctan2(-ax, np.sqrt(ay**2 + az**2)) * 180 / np.pi

            # Update angles from gyro
            gyro_angles[0] += gx * dt
            gyro_angles[1] += gy * dt
            gyro_angles[2] += gz * dt

            # Apply complementary filter
            alpha = 0.98
            roll = alpha * gyro_angles[0] + (1 - alpha) * roll_acc
            pitch = alpha * gyro_angles[1] + (1 - alpha) * pitch_acc
            yaw = gyro_angles[2]  # Yaw hanya diperbarui dengan gyro

            # Append result to list
            euler_angles_list.append([imu_data['timestamps'][i], roll, pitch, yaw])
        return euler_angles_list

    def convert_to_impact(self, imu_data, mass, gravity=9.8):
        accel_data = np.column_stack((imu_data['acc_x'], imu_data['acc_y'], imu_data['acc_z']))
        impact_forces = np.zeros(len(accel_data))
        total_accelerations = np.zeros(len(accel_data))

        for i, accel in enumerate(accel_data):
            accel_x, accel_y, accel_z = accel
            # accel_z -= gravity  # Compensate for gravity
            total_acceleration = math.sqrt(accel_x**2 + accel_y**2 + accel_z**2)
            impact_forces[i] = mass * total_acceleration
            total_accelerations[i] = total_acceleration

        return impact_forces, total_accelerations

if __name__ == "__main__": 
    imu_file = "Data_Sample/sample_imu_raw.csv"
    imu_dataCSV = pd.read_csv(imu_file)
    rows_imu = imu_dataCSV.values.tolist()
    imu_data = {
        "timestamps": [row[0] for row in rows_imu],
        "acc_x": [row[1] for row in rows_imu],
        "acc_y": [row[2] for row in rows_imu],
        "acc_z": [row[3] for row in rows_imu],
    }
    if imu_dataCSV is not None:
        conn = Connection()
        impact_forces, total_accelerations = conn.convert_to_impact(imu_data, mass=3)
        
        # Output the results
        for i in range(len(impact_forces)):
            print(impact_forces[i], total_accelerations[i])
            # print(f"Sample {i}: Impact Force = {impact_forces[i]} N, Total Acceleration = {total_accelerations[i]} m/s²")
    else:
        print("Failed to read IMU data.")
