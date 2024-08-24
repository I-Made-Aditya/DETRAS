import os
import cv2
import sys
import math
from PySide6 import QtCharts
from PySide6.QtCore import Qt, QTimer, QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QFileDialog, QTableWidgetItem, QListWidgetItem
from PySide6.QtGui import QPixmap, QImage, QSurfaceFormat
from PySide6.QtDataVisualization import Q3DBars, QBar3DSeries, QBarDataItem, QCategory3DAxis, QValue3DAxis
from PySide6.QtWebEngineWidgets import QWebEngineView
import scipy as sp
from openglwidget import OpenGLWidget
import folium
from folium.plugins import AntPath
import io
import pandas as pd
from interface import Ui_MainWindow
from gait_tracking import Trajectory
from camera import FacialEmotionRecognition

# Import Custom widgets
from Custom_Widgets.Widgets import *

# Import database connection functions
from database import Connection

size_camera = QSize(600, 400)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)

        self.obdCSV = None
        self.impactCSV = None
        self.imuCSV = None
        self.quaternionCSV = None
        self.eulerCSV = None
        self.gpsCSV = None
        self.videoMP4 = None
        self.cap = None
        self.timer = QTimer()

        self.trajWid = None
        self.openglwidget = None

        self.model_json_path = "fer.json"
        self.model_weights_path = "fer.h5" 
        self.haar_cascade_path = "haarcascade_frontalface_default.xml"
        self.default_image_path = 'tumbnail.jpg'

        # Initialize FacialEmotionRecognition
        self.fer = FacialEmotionRecognition(
            model_json_path=self.model_json_path,
            model_weights_path=self.model_weights_path,
            haar_cascade_path=cv2.data.haarcascades + self.haar_cascade_path
        )

        # Browse file
        self.ui.obdfilebtn.clicked.connect(self.obdLoadData)
        self.ui.impactfilebtn.clicked.connect(self.impactLoadData)
        self.ui.rawinerfilebtn.clicked.connect(self.imuLoadData)
        self.ui.quaternionfilebtn.clicked.connect(self.quaternionLoadData)
        self.ui.eulerfilebtn.clicked.connect(self.eulerLoadData)
        self.ui.gpsfilebtn.clicked.connect(self.gpsLoadData)
        self.ui.camerafilebtn.clicked.connect(self.cameraLoadData)
        
        self.ui.showDataOBDcsv.clicked.connect(self.TableShowDataOBD)
        self.ui.impactupBtn.clicked.connect(self.TableShowDataImpact)
        self.ui.rawinerupBtn.clicked.connect(self.TableShowDataIMU)
        self.ui.quaternionupBtn.clicked.connect(self.TableShowDataQuaternion)
        self.ui.eulerupBtn.clicked.connect(self.TableShowDataEuler)
        self.ui.gpsupBtn.clicked.connect(self.TableShowDataGPS)
        

        self.ui.vCam = QLabel(self.ui.vCam)
        self.ui.vCam.setGeometry(100, 10, size_camera.width(), size_camera.height())
        self.load_default_image()
        self.ui.onCambtn.clicked.connect(self.start_camera)
        self.ui.offCambtn.clicked.connect(self.stop_camera)

        self.ui.simulationPlay.clicked.connect(self.SimulationStart)
        self.ui.simulationStop.clicked.connect(self.SimulationStop)

#====================================================================================================================
#====================================================================================================================
    def obdLoadData(self):
        csvfile, _ = QFileDialog.getOpenFileName(self, 'Open File', 'D:', 'CSV files (*.csv)')
        if csvfile:  # Check if a file was selected
            self.obdCSV = pd.read_csv(csvfile)
            self.ui.OBDfilebrowse.setText(csvfile)
            # self.OBDfile = csvfile
    
    def impactLoadData(self):
        csvfile, _ = QFileDialog.getOpenFileName(self, 'Open File', 'D:', 'CSV files (*.csv)')
        if csvfile:  # Check if a file was selected
            self.impactCSV = pd.read_csv(csvfile)
            self.ui.impactfilebrowse.setText(csvfile)
            # self.Impactfile = csvfile

    def imuLoadData(self):
        csvfile, _ = QFileDialog.getOpenFileName(self, 'Open File', 'D:', 'CSV files (*.csv)')
        if csvfile:  # Check if a file was selected
            self.imuCSV = pd.read_csv(csvfile)
            self.ui.rawinerfilebrowse.setText(csvfile)
            # self.Impactfile = csvfile

    def quaternionLoadData(self):
        csvfile, _ = QFileDialog.getOpenFileName(self, 'Open File', 'D:', 'CSV files (*.csv)')
        if csvfile:  # Check if a file was selected
            self.quaternionCSV = pd.read_csv(csvfile)
            self.ui.quaternionfilebrowse.setText(csvfile)
            # self.Impactfile = csvfile
    
    def eulerLoadData(self):
        csvfile, _ = QFileDialog.getOpenFileName(self, 'Open File', 'D:', 'CSV files (*.csv)')
        if csvfile:  # Check if a file was selected
            self.eulerCSV = pd.read_csv(csvfile)
            self.ui.eulerfilebrowse.setText(csvfile)
            # self.Impactfile = csvfile

    def gpsLoadData(self):
        csvfile, _ = QFileDialog.getOpenFileName(self, 'Open File', 'D:', 'CSV files (*.csv)')
        if csvfile:  # Check if a file was selected
            self.gpsCSV = pd.read_csv(csvfile)
            self.ui.gpsfilebrowse.setText(csvfile)
            # self.Impactfile = csvfile
    #Camera
    def cameraLoadData(self):
        video_formats = "Video files (*.mp4 *.avi *.mov *.mkv *.flv *.wmv)"
        mp4file, _ = QFileDialog.getOpenFileName(self, 'Open File', 'D:', video_formats)
        if mp4file:  # Check if a file was selected
            self.videoMP4 = mp4file
            self.ui.camerafilebrowse.setText(mp4file)
#====================================================================================================================
#====================================================================================================================
    def TableShowDataOBD(self):
        if self.obdCSV is not None:  # Ensure data is loaded
            rows_obd = self.obdCSV.values.tolist()
            self.ui.obdData1.setRowCount(len(rows_obd))
            self.ui.obdData2.setRowCount(len(rows_obd))

            table_row1 = 0
            for row in rows_obd:
                for col in range(0, 3):  # Mengisi hanya kolom 1-3
                    self.ui.obdData1.setItem(table_row1, col, QTableWidgetItem(str(row[col])))
                table_row1 += 1
            self.obd1_update_linechart()
            table_row2 = 0
            for row in rows_obd:
                for col_index, col in enumerate(range(3, 5)):  # Mengisi hanya kolom 4-5
                    self.ui.obdData2.setItem(table_row2, col_index, QTableWidgetItem(str(row[col])))
                table_row2 += 1
            self.obd2_update_linechart()
            self.ui.obdData2.resizeColumnsToContents()
        else:
            print("Error loading OBD-II data: No data loaded")
    
    def TableShowDataImpact(self):
        if self.impactCSV is not None:  # Ensure data is loaded
            rows_iner = self.impactCSV.values.tolist()
            self.ui.ImpactTable.setRowCount(len(rows_iner))

            table_row = 0
            for row in rows_iner:
                for col in range(0, 3):  # Mengisi hanya kolom 1-3
                    self.ui.ImpactTable.setItem(table_row, col, QTableWidgetItem(str(row[col])))
                table_row += 1
            self.impact_update_linechart()
        else:
            print("Error loading Impact data: No data loaded")

    def TableShowDataIMU(self):
        if self.imuCSV is not None:  # Ensure data is loaded
            rows_imu = self.imuCSV.values.tolist()
            self.ui.inertialTable.setRowCount(len(rows_imu))
            self.ui.inertialTable.setColumnCount(9)

            table_row = 0
            for row in rows_imu:
                for col in range(1, 10):  # Mengisi hanya kolom 1-3
                    self.ui.inertialTable.setItem(table_row, col-1, QTableWidgetItem(str(row[col])))
                table_row += 1
            self.imu_raw_update_linechart()
        else:
            print("Error loading Inertial data: No data loaded")

    def TableShowDataQuaternion(self):
        
        if self.quaternionCSV is not None:  # Ensure data is loaded
            rows_quaternion = self.quaternionCSV.values.tolist()
            self.ui.quaternionTable.setRowCount(len(rows_quaternion))
            self.ui.quaternionTable.setColumnCount(4)

            table_row = 0
            for row in rows_quaternion:
                for col in range(1, 5):  # Mengisi hanya kolom 1-4
                    self.ui.quaternionTable.setItem(table_row, col-1, QTableWidgetItem(str(row[col])))
                table_row += 1
            self.quaternion_update_linechart()
        else:
            print("Error loading Quaternion data: No data loaded")

    def TableShowDataEuler(self):
        if self.eulerCSV is not None:  # Ensure data is loaded
            rows_euler = self.eulerCSV.values.tolist()
            self.ui.eulerTable.setRowCount(len(rows_euler))
            self.ui.eulerTable.setColumnCount(3)

            table_row = 0
            for row in rows_euler:
                for col in range(1, 4):  # Mengisi hanya kolom 1-4
                    self.ui.eulerTable.setItem(table_row, col-1, QTableWidgetItem(str(row[col])))
                table_row += 1
            self.euler_update_linechart()
        else:
            print("Error loading Euler data: No data loaded")
    
    def TableShowDataGPS(self):
        if self.gpsCSV is not None:  # Ensure data is loaded
            rows_gps = self.gpsCSV.values.tolist()
            self.ui.gpsTable.setRowCount(len(rows_gps))
            self.ui.gpsTable.setColumnCount(2)

            table_row = 0
            for row in rows_gps:
                for col in range(1, 3):  # Mengisi hanya kolom 1-4
                    self.ui.gpsTable.setItem(table_row, col-1, QTableWidgetItem(str(row[col])))
                table_row += 1
            self.ui.gpsTable.resizeColumnsToContents()
            self.GPSmaps()
        else:
            print("Error loading GPS data: No data loaded")
#====================================================================================================================
#====================================================================================================================
    def imu_raw_update_linechart(self):
        lineChart = QtCharts.QChart()
        rows_imu = self.imuCSV.values.tolist()

        accel_x = [row[1] for row in rows_imu]
        accel_y = [row[2] for row in rows_imu]
        accel_z = [row[3] for row in rows_imu]

        gyro_x = [row[4] for row in rows_imu]
        gyro_y = [row[5] for row in rows_imu]
        gyro_z = [row[6] for row in rows_imu]

        mag_x = [row[7] for row in rows_imu]
        mag_y = [row[8] for row in rows_imu]
        mag_z = [row[9] for row in rows_imu]
        
        accel_x_series = QtCharts.QLineSeries()
        accel_x_series.setName("Accel_x")
        for i in range(len(rows_imu)):
            accel_x_series.append(i, accel_x[i])
        lineChart.addSeries(accel_x_series)

        accel_y_series = QtCharts.QLineSeries()
        accel_y_series.setName("Accel_y")
        for i in range(len(rows_imu)):
            accel_y_series.append(i, accel_y[i])
        lineChart.addSeries(accel_y_series)

        accel_z_series = QtCharts.QLineSeries()
        accel_z_series.setName("Accel_z")
        for i in range(len(rows_imu)):
            accel_z_series.append(i, accel_z[i])
        lineChart.addSeries(accel_z_series)

        gyro_x_series = QtCharts.QLineSeries()
        gyro_x_series.setName("Gyro_x")
        for i in range(len(rows_imu)):
            gyro_x_series.append(i, gyro_x[i])
        lineChart.addSeries(gyro_x_series)

        gyro_y_series = QtCharts.QLineSeries()
        gyro_y_series.setName("Gyro_y")
        for i in range(len(rows_imu)):
            gyro_y_series.append(i, gyro_y[i])
        lineChart.addSeries(gyro_y_series)

        gyro_z_series = QtCharts.QLineSeries()
        gyro_z_series.setName("Gyro_z")
        for i in range(len(rows_imu)):
            gyro_z_series.append(i, gyro_z[i])
        lineChart.addSeries(gyro_z_series)

        mag_x_series = QtCharts.QLineSeries()
        mag_x_series.setName("Mag_x")
        for i in range(len(rows_imu)):
            mag_x_series.append(i, mag_x[i])
        lineChart.addSeries(mag_x_series)

        mag_y_series = QtCharts.QLineSeries()
        mag_y_series.setName("Mag_y")
        for i in range(len(rows_imu)):
            mag_y_series.append(i, mag_y[i])
        lineChart.addSeries(mag_y_series)

        mag_z_series = QtCharts.QLineSeries()
        mag_z_series.setName("Mag_z")
        for i in range(len(rows_imu)):
            mag_z_series.append(i, mag_z[i])
        lineChart.addSeries(mag_z_series)

        axis_x = QtCharts.QBarCategoryAxis()
        axis_x.append(rows_imu)
        lineChart.addAxis(axis_x, Qt.AlignBottom)

        axis_y = QtCharts.QValueAxis()

        min_y = min(min(accel_x), min(accel_y), min(accel_z), min(gyro_x), min(gyro_y), min(gyro_z), min(mag_x), min(mag_y), min(mag_z))
        max_y = max(max(accel_x), max(accel_y), max(accel_z), max(gyro_x), max(gyro_y), max(gyro_z), max(mag_x), max(mag_y), max(mag_z))
        axis_y.setRange(min_y, max_y)
        lineChart.addAxis(axis_y, Qt.AlignLeft)

        accel_x_series.attachAxis(axis_x)
        accel_x_series.attachAxis(axis_y)
        accel_y_series.attachAxis(axis_x)
        accel_y_series.attachAxis(axis_y)
        accel_z_series.attachAxis(axis_x)
        accel_z_series.attachAxis(axis_y)

        gyro_x_series.attachAxis(axis_x)
        gyro_x_series.attachAxis(axis_y)
        gyro_y_series.attachAxis(axis_x)
        gyro_y_series.attachAxis(axis_y)
        gyro_z_series.attachAxis(axis_x)
        gyro_z_series.attachAxis(axis_y)

        mag_x_series.attachAxis(axis_x)
        mag_x_series.attachAxis(axis_y)
        mag_y_series.attachAxis(axis_x)
        mag_y_series.attachAxis(axis_y)
        mag_z_series.attachAxis(axis_x)
        mag_z_series.attachAxis(axis_y)

        self.ui.ImuChart.setChart(lineChart)

    def quaternion_update_linechart(self):
        lineChart = QtCharts.QChart()
        rows_imu = self.quaternionCSV.values.tolist()

        q1 = [row[1] for row in rows_imu]
        q2 = [row[2] for row in rows_imu]
        q3 = [row[3] for row in rows_imu]
        q4 = [row[4] for row in rows_imu]

        q1_series = QtCharts.QLineSeries()
        q1_series.setName("Q1")
        for i in range(len(rows_imu)):
            q1_series.append(i, q1[i])
        lineChart.addSeries(q1_series)

        q2_series = QtCharts.QLineSeries()
        q2_series.setName("Q2")
        for i in range(len(rows_imu)):
            q2_series.append(i, q2[i])
        lineChart.addSeries(q2_series)

        q3_series = QtCharts.QLineSeries()
        q3_series.setName("Q3")
        for i in range(len(rows_imu)):
            q3_series.append(i, q3[i])
        lineChart.addSeries(q3_series)

        q4_series = QtCharts.QLineSeries()
        q4_series.setName("Q4")
        for i in range(len(rows_imu)):
            q4_series.append(i, q4[i])
        lineChart.addSeries(q4_series)

        axis_x = QtCharts.QBarCategoryAxis()
        axis_x.append(rows_imu)
        lineChart.addAxis(axis_x, Qt.AlignBottom)

        axis_y = QtCharts.QValueAxis()

        min_y = min(min(q1), min(q2), min(q3), min(q4))
        max_y = max(max(q1), max(q2), max(q3), max(q4))
        axis_y.setRange(min_y, max_y)
        lineChart.addAxis(axis_y, Qt.AlignLeft)

        q1_series.attachAxis(axis_x)
        q1_series.attachAxis(axis_y)

        q2_series.attachAxis(axis_x)
        q2_series.attachAxis(axis_y)
        
        q3_series.attachAxis(axis_x)
        q3_series.attachAxis(axis_y)

        q4_series.attachAxis(axis_x)
        q4_series.attachAxis(axis_y)

        self.ui.quaternionChart.setChart(lineChart)
    
    def euler_update_linechart(self):
        lineChart = QtCharts.QChart()
        rows_imu = self.eulerCSV.values.tolist()

        roll = [row[1] for row in rows_imu]
        pitch = [row[2] for row in rows_imu]
        yaw = [row[3] for row in rows_imu]

        roll_series = QtCharts.QLineSeries()
        roll_series.setName("Roll")
        for i in range(len(rows_imu)):
            roll_series.append(i, roll[i])
        lineChart.addSeries(roll_series)

        pitch_series = QtCharts.QLineSeries()
        pitch_series.setName("Pitch")
        for i in range(len(rows_imu)):
            pitch_series.append(i, pitch[i])
        lineChart.addSeries(pitch_series)

        yaw_series = QtCharts.QLineSeries()
        yaw_series.setName("Yaw")
        for i in range(len(rows_imu)):
            yaw_series.append(i, yaw[i])
        lineChart.addSeries(yaw_series)

        axis_x = QtCharts.QBarCategoryAxis()
        axis_x.append(rows_imu)
        lineChart.addAxis(axis_x, Qt.AlignBottom)

        axis_y = QtCharts.QValueAxis()

        min_y = min(min(roll), min(pitch), min(yaw))
        max_y = max(max(roll), max(pitch), max(yaw))
        axis_y.setRange(min_y, max_y)
        lineChart.addAxis(axis_y, Qt.AlignLeft)

        roll_series.attachAxis(axis_x)
        roll_series.attachAxis(axis_y)

        pitch_series.attachAxis(axis_x)
        pitch_series.attachAxis(axis_y)
        
        yaw_series.attachAxis(axis_x)
        yaw_series.attachAxis(axis_y)

        self.ui.EulerChart.setChart(lineChart)
    
    def impact_update_linechart(self):
        lineChart = QtCharts.QChart()
        rows_impact = self.impactCSV.values.tolist()

        Taccel = [row[1] for row in rows_impact]
        impact = [row[2] for row in rows_impact]

        Taccel_series = QtCharts.QLineSeries()
        Taccel_series.setName("Total Acceleration")
        for i in range(len(rows_impact)):
            Taccel_series.append(i,   Taccel[i])
        lineChart.addSeries(Taccel_series)

        impact_series = QtCharts.QLineSeries()
        impact_series.setName("Impact")
        for i in range(len(rows_impact)):
            impact_series.append(i, impact[i])
        lineChart.addSeries(impact_series)

        axis_x = QtCharts.QBarCategoryAxis()
        axis_x.append(rows_impact)
        lineChart.addAxis(axis_x, Qt.AlignBottom)

        axis_y = QtCharts.QValueAxis()

        min_y = min(Taccel)
        max_y = max(Taccel)

        axis_y.setRange(min_y, max_y)
        lineChart.addAxis(axis_y, Qt.AlignLeft)

        Taccel_series.attachAxis(axis_x)
        Taccel_series.attachAxis(axis_y)

        impact_series.attachAxis(axis_x)
        impact_series.attachAxis(axis_y)

        self.ui.ImpactChart.setChart(lineChart)
        # pass

    def obd1_update_linechart(self):
        lineChart1 = QtCharts.QChart()
        lineChart2 = QtCharts.QChart()
        lineChart3 = QtCharts.QChart()
        rows_imu = self.obdCSV.values.tolist()

        rpm = [row[0] for row in rows_imu]
        coolant = [row[1] for row in rows_imu]
        oil_temp = [row[2] for row in rows_imu]

        rpm_series = QtCharts.QLineSeries()
        rpm_series.setName("Engine (rpm)")
        for i in range(len(rows_imu)):
            rpm_series.append(i,   rpm[i])
        lineChart1.addSeries(rpm_series)

        coolant_series = QtCharts.QLineSeries()
        coolant_series.setName("Coolant Temperature")
        for i in range(len(rows_imu)):
            coolant_series.append(i, coolant[i])
        lineChart2.addSeries(coolant_series)

        oil_temp_series = QtCharts.QLineSeries()
        oil_temp_series.setName("Oil Temperature")
        for i in range(len(rows_imu)):
            oil_temp_series.append(i, oil_temp[i])
        lineChart3.addSeries(oil_temp_series)

        axis_x1 = QtCharts.QBarCategoryAxis()
        axis_x1.append(rows_imu)
        lineChart1.addAxis(axis_x1, Qt.AlignBottom)

        axis_x2 = QtCharts.QBarCategoryAxis()
        axis_x2.append(rows_imu)
        lineChart2.addAxis(axis_x2, Qt.AlignBottom)

        axis_x3 = QtCharts.QBarCategoryAxis()
        axis_x3.append(rows_imu)
        lineChart3.addAxis(axis_x3, Qt.AlignBottom)

        axis_y1 = QtCharts.QValueAxis()
        axis_y2 = QtCharts.QValueAxis()
        axis_y3 = QtCharts.QValueAxis()

        min_y1 = min(rpm)
        max_y1 = max(rpm)

        min_y2 = min(coolant)
        max_y2 = max(coolant)

        min_y3 = min(oil_temp)
        max_y3 = max(oil_temp)

        axis_y1.setRange(min_y1, max_y1)
        lineChart1.addAxis(axis_y1, Qt.AlignLeft)
        axis_y2.setRange(min_y2, max_y2)
        lineChart2.addAxis(axis_y2, Qt.AlignLeft)
        axis_y3.setRange(min_y3, max_y3)
        lineChart3.addAxis(axis_y3, Qt.AlignLeft)

        rpm_series.attachAxis(axis_x1)
        rpm_series.attachAxis(axis_y1)

        coolant_series.attachAxis(axis_x2)
        coolant_series.attachAxis(axis_y2)
        
        oil_temp_series.attachAxis(axis_x3)
        oil_temp_series.attachAxis(axis_y3)

        self.ui.rpmChart.setChart(lineChart1)
        self.ui.coolantChart.setChart(lineChart2)
        self.ui.olitempChart.setChart(lineChart3)
        # pass

    def obd2_update_linechart(self):
        lineChart1 = QtCharts.QChart()
        lineChart2 = QtCharts.QChart()
        rows_obd2 = self.obdCSV.values.tolist()

        speed = [row[3] for row in rows_obd2]
        throttle = [row[4] for row in rows_obd2]

        speed_series = QtCharts.QLineSeries()
        speed_series.setName("Speed")
        speedCostumC = QColor("orange")
        speed_series.setColor(speedCostumC)
        for i in range(len(rows_obd2)):
            speed_series.append(i,   speed[i])
        lineChart1.addSeries(speed_series)

        throttle_series = QtCharts.QLineSeries()
        throttle_series.setName("Throttle")
        # gpsSpeedCostumC = QColor("read")
        # rpm_series.setColor(gpsSpeedCostumC)
        for i in range(len(rows_obd2)):
            throttle_series.append(i, throttle[i])
        lineChart2.addSeries(throttle_series)

        axis_x1 = QtCharts.QBarCategoryAxis()
        axis_x1.append(rows_obd2)
        lineChart1.addAxis(axis_x1, Qt.AlignBottom)

        axis_x2 = QtCharts.QBarCategoryAxis()
        axis_x2.append(rows_obd2)
        lineChart2.addAxis(axis_x2, Qt.AlignBottom)

        axis_y1 = QtCharts.QValueAxis()
        axis_y2 = QtCharts.QValueAxis()

        min_y1 = min(speed)
        max_y1 = max(speed)
        axis_y1.setRange(min_y1, max_y1)
        lineChart1.addAxis(axis_y1, Qt.AlignLeft)

        min_y2 = min(throttle)
        max_y2 = max(throttle)
        axis_y2.setRange(min_y2, max_y2)
        lineChart2.addAxis(axis_y2, Qt.AlignLeft)

        speed_series.attachAxis(axis_x1)
        speed_series.attachAxis(axis_y1)

        throttle_series.attachAxis(axis_x2)
        throttle_series.attachAxis(axis_y2)

        self.ui.speedChart.setChart(lineChart1)
        self.ui.throttleChart.setChart(lineChart2)
        # pass
#====================================================================================================================
#====================================================================================================================
    def load_default_image(self):
        pixmap = QPixmap(self.default_image_path)
        self.ui.vCam.setPixmap(pixmap.scaled(size_camera, Qt.KeepAspectRatio))

    def start_camera(self):
        if self.videoMP4 is not None:
            # self.cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
            self.cap = cv2.VideoCapture(self.videoMP4)
            self.timer.start(10)
            # print("Bisa load camera")
            self.timer.timeout.connect(self.update_frame)
            
    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            # Detect emotions
            frame = self.fer.detect_emotions(frame)
            # Resize frame to fit QLabel
            frame_resized = cv2.resize(frame, (size_camera.width(), size_camera.height()))
            # Convert frame to QImage
            frame_rgb = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2RGB)
            h, w, ch = frame_rgb.shape
            bytes_per_line = ch * w
            q_img = QImage(frame_rgb.data, w, h, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(q_img)
            self.ui.vCam.setPixmap(pixmap)
        
        # Get predictions and display in QListWidget
        predic = self.fer.showPredic()  # Assuming showPredic method doesn't need an argument
        listFER = QListWidgetItem(predic)
        self.ui.FERview.addItem(listFER)
        # print(predic)
            
    def stop_camera(self):
        if self.cap:
            self.cap.release()
            self.cap = None
        self.timer.stop()
        self.load_default_image()
#====================================================================================================================
    def GPSmaps(self):
        gpsrow_file = self.gpsCSV.values.tolist()
        longitudes = [row[1] for row in gpsrow_file]  # Assuming row[1] is longitude
        latitudes = [row[2] for row in gpsrow_file]  # Assuming row[2] is latitude

        lat_lngs = list(zip(longitudes, latitudes))
        if lat_lngs:
            Location = [sum(longitudes) / len(longitudes), sum(latitudes) / len(latitudes)]
        else:
            Location = [-7.276672642751252, 112.7943296600885]  # Default location if no data
        
        m = folium.Map(
            tiles='OpenStreetMap',
            zoom_start=15,
            location=Location
        )
        # Menambahkan marker untuk setiap titik
        for lng, lat in lat_lngs:
            folium.Marker(location=[lng, lat]).add_to(m)

        # Menambahkan AntPath untuk menunjukkan arah perjalanan
        AntPath(lat_lngs, color='blue', weight=2.5, opacity=1).add_to(m)
        mapsData = io.BytesIO()
        m.save(mapsData, close_file=False)
        webView = QWebEngineView()
        webView.setHtml(mapsData.getvalue().decode())
        layout = self.ui.mapsWidget.layout()
        layout.addWidget(webView)
#====================================================================================================================
    def SimulationStart(self):
        if self.imuCSV is not None:
            rows_imu = self.imuCSV.values.tolist()
            imu_data = {
                "timestamps": [row[0] for row in rows_imu],
                "accel_x": [row[1] for row in rows_imu],
                "accel_y": [row[2] for row in rows_imu],
                "accel_z": [row[3] for row in rows_imu],
                "gyro_x": [row[4] for row in rows_imu],
                "gyro_y": [row[5] for row in rows_imu],
                "gyro_z": [row[6] for row in rows_imu],
            }
            self.trajWid = Trajectory(imu_data=imu_data)
            self.trajectory_layout = self.ui.widgetTrajectory.layout()
            self.trajectory_layout.addWidget(self.trajWid)

        if self.eulerCSV is not None:
            rows_euler = self.eulerCSV.values.tolist()
            euler = {
                "timestamp": [row[0] for row in rows_euler],
                "roll": [row[1] for row in rows_euler],
                "pitch": [row[2] for row in rows_euler],
                "yaw": [row[3] for row in rows_euler],
            }
            self.openglwidget = OpenGLWidget(euler_data=euler)
            self.opengl = self.ui.widgetOrientaion.layout()
            self.opengl.addWidget(self.openglwidget)

#====================================================================================================================
    def SimulationStop(self):
        if self.trajWid is not None:
            self.trajectory_layout.removeWidget(self.trajWid)
            self.trajWid.setParent(None)
            self.trajWid.deleteLater()
            self.trajWid = None

        if self.openglwidget is not None:
            self.opengl.removeWidget(self.openglwidget)
            self.openglwidget.setParent(None)
            self.openglwidget.deleteLater()
            self.openglwidget = None

#====================================================================================================================
#====================================================================================================================
if __name__ == "__main__":
    # Set the environment variable for the graphics backend
    os.environ['QSG_RHI_BACKEND'] = 'opengl'  # Can be 'opengl', 'vulkan', 'metal', etc.

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
