import csv
import time
import board
import busio
import numpy as np
import adafruit_fxos8700
import adafruit_fxas21002c
from ahrs.filters import EKF
import threading

# Inisialisasi I2C dan sensor
i2c = board.I2C()  # Menggunakan board.SCL dan board.SDA

AM_sensor = adafruit_fxos8700.FXOS8700(i2c, accel_range=adafruit_fxos8700.ACCEL_RANGE_8G)
G_sensor = adafruit_fxas21002c.FXAS21002C(i2c, gyro_range=adafruit_fxas21002c.GYRO_RANGE_2000DPS)

# Inisialisasi filter EKF
ekf = EKF()

# Inisialisasi quaternion awal dengan norm 1
q = np.array([1.0, 0.0, 0.0, 0.0])
q /= np.linalg.norm(q)

def record_data_to_csv(file_path):
    global q  # Menandakan variabel q adalah variabel global

    with open(file_path, 'w', newline='') as csvfile:
        fieldnames = ['q_w', 'q_x', 'q_y', 'q_z']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        data_count = 0  # Untuk menghitung jumlah data yang sudah direkam
        try: 

            while True:
                # Baca data accelerometer, gyroscope, dan magnetometer
                accel_x, accel_y, accel_z = AM_sensor.accelerometer
                gyro_x, gyro_y, gyro_z = G_sensor.gyroscope
                mag_x, mag_y, mag_z = AM_sensor.magnetometer

                # Konversi nilai akselerometer ke g (gravitasi)
                accel_x_g = accel_x / adafruit_fxos8700._SENSORS_GRAVITY_STANDARD
                accel_y_g = accel_y / adafruit_fxos8700._SENSORS_GRAVITY_STANDARD
                accel_z_g = accel_z / adafruit_fxos8700._SENSORS_GRAVITY_STANDARD

                # Data input untuk filter EKF
                accel_data = np.array([accel_x_g, accel_y_g, accel_z_g])
                gyro_data = np.array([gyro_x, gyro_y, gyro_z])
                mag_data = np.array([mag_x, mag_y, mag_z])

                # Pastikan quaternion memiliki norm 1
                if np.linalg.norm(q) != 1.0:
                    q /= np.linalg.norm(q)

                # Perbarui quaternion dengan filter EKF
                q = ekf.update(q, gyr=gyro_data, acc=accel_data, mag=mag_data)

                # Cetak komponen quaternion: w, x, y, z
                w, x, y, z = q
                print(f"Quaternion: w:{w:0.3f}, x:{x:0.3f}, y:{y:0.3f}, z:{z:0.3f}")

                writer.writerow({'q_w': w,
                                'q_x': x,
                                'q_y': y,
                                'q_z': z})
                    
                print("Data ditulis ke file CSV.")
                data_count += 1
                time.sleep(0.01)

        except KeyboardInterrupt:
            print("Recording stopped.")
            
if __name__ == "__main__":
    # Start recording data
    record_thread = threading.Thread(target=record_data_to_csv, args=('imu_qua.csv',))
    record_thread.daemon = True
    record_thread.start()
    
    while True:
        time.sleep(0.01)
