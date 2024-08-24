# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCharts import QChartView
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 650)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 650))
        MainWindow.setMaximumSize(QSize(1000, 787))
        MainWindow.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	background: none;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #000000;\n"
"}\n"
"#centralwidget{\n"
"	background-color:#FFFFFF;\n"
"}\n"
"#LeftMenuSubContainer{\n"
"	background-color:#e3e3e3;\n"
"}\n"
"#LeftMenuSubContainer QPushButton{\n"
"	text-align: left;\n"
"	padding: 5px 10px;\n"
"	border-top-left-radius:10px;\n"
"	border-bottom-left-radius:10px;\n"
"}\n"
"#headerContainer, #footerContainer{\n"
"	background-color:#e3e3e3;\n"
"}\n"
"#popupNotificationSubContainer{\n"
"	background-color:#e3e3e3;\n"
"	border-radius: 10px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.LeftMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.LeftMenuContainer.setObjectName(u"LeftMenuContainer")
        self.LeftMenuContainer.setMaximumSize(QSize(55, 16777215))
        self.verticalLayout = QVBoxLayout(self.LeftMenuContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.LeftMenuSubContainer = QWidget(self.LeftMenuContainer)
        self.LeftMenuSubContainer.setObjectName(u"LeftMenuSubContainer")
        self.verticalLayout_2 = QVBoxLayout(self.LeftMenuSubContainer)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.frame = QFrame(self.LeftMenuSubContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menuBtn = QPushButton(self.frame)
        self.menuBtn.setObjectName(u"menuBtn")
        icon = QIcon()
        icon.addFile(u":/icons/icons/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.menuBtn)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.LeftMenuSubContainer)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.homebtn = QPushButton(self.frame_2)
        self.homebtn.setObjectName(u"homebtn")
        self.homebtn.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homebtn.setIcon(icon1)
        self.homebtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.homebtn)

        self.obdbtn = QPushButton(self.frame_2)
        self.obdbtn.setObjectName(u"obdbtn")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/bluetooth.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.obdbtn.setIcon(icon2)
        self.obdbtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.obdbtn)

        self.imusbtn = QPushButton(self.frame_2)
        self.imusbtn.setObjectName(u"imusbtn")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/globe.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.imusbtn.setIcon(icon3)
        self.imusbtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.imusbtn)

        self.gpsbtn = QPushButton(self.frame_2)
        self.gpsbtn.setObjectName(u"gpsbtn")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/send.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.gpsbtn.setIcon(icon4)
        self.gpsbtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.gpsbtn)

        self.cambtn = QPushButton(self.frame_2)
        self.cambtn.setObjectName(u"cambtn")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/camera.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.cambtn.setIcon(icon5)
        self.cambtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.cambtn)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.LeftMenuSubContainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.helpbtn = QPushButton(self.frame_3)
        self.helpbtn.setObjectName(u"helpbtn")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.helpbtn.setIcon(icon6)
        self.helpbtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.helpbtn)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.LeftMenuSubContainer)


        self.horizontalLayout.addWidget(self.LeftMenuContainer)

        self.mainBodyContainer = QCustomSlideMenu(self.centralwidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy2)
        self.mainBodyContainer.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.headerContainer = QWidget(self.mainBodyContainer)
        self.headerContainer.setObjectName(u"headerContainer")
        font = QFont()
        font.setFamilies([u"MS Shell Dlg 2"])
        font.setPointSize(9)
        self.headerContainer.setFont(font)
        self.verticalLayout_6 = QVBoxLayout(self.headerContainer)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_4 = QFrame(self.headerContainer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 3, 0, 0)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMaximumSize(QSize(120, 120))
        font1 = QFont()
        font1.setFamilies([u"Imprint MT Shadow"])
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setItalic(False)
        self.label.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_6.addWidget(self.frame_4, 0, Qt.AlignLeft)


        self.verticalLayout_5.addWidget(self.headerContainer)

        self.mainBodyContent = QWidget(self.mainBodyContainer)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy3)
        self.verticalLayout_7 = QVBoxLayout(self.mainBodyContent)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.mainPages = QStackedWidget(self.mainBodyContent)
        self.mainPages.setObjectName(u"mainPages")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.mainPages.sizePolicy().hasHeightForWidth())
        self.mainPages.setSizePolicy(sizePolicy4)
        self.mainPages.setMinimumSize(QSize(945, 0))
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.verticalLayout_8 = QVBoxLayout(self.homePage)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_2 = QLabel(self.homePage)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setFamilies([u"RomanC"])
        font2.setPointSize(24)
        font2.setBold(True)
        font2.setItalic(False)
        self.label_2.setFont(font2)
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_2)

        self.mainPages.addWidget(self.homePage)
        self.obdPage = QWidget()
        self.obdPage.setObjectName(u"obdPage")
        self.verticalLayout_9 = QVBoxLayout(self.obdPage)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.obdPages = QStackedWidget(self.obdPage)
        self.obdPages.setObjectName(u"obdPages")
        self.LoadOBD = QWidget()
        self.LoadOBD.setObjectName(u"LoadOBD")
        self.verticalLayout_15 = QVBoxLayout(self.LoadOBD)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.judulOBD_3 = QWidget(self.LoadOBD)
        self.judulOBD_3.setObjectName(u"judulOBD_3")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.judulOBD_3.sizePolicy().hasHeightForWidth())
        self.judulOBD_3.setSizePolicy(sizePolicy5)
        self.horizontalLayout_24 = QHBoxLayout(self.judulOBD_3)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(20, 0, 20, 0)
        self.Judul_3 = QLabel(self.judulOBD_3)
        self.Judul_3.setObjectName(u"Judul_3")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.Judul_3.setFont(font3)

        self.horizontalLayout_24.addWidget(self.Judul_3)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_13)

        self.LoadFileOBD = QPushButton(self.judulOBD_3)
        self.LoadFileOBD.setObjectName(u"LoadFileOBD")
        font4 = QFont()
        font4.setBold(True)
        self.LoadFileOBD.setFont(font4)

        self.horizontalLayout_24.addWidget(self.LoadFileOBD)

        self.horizontalSpacer_15 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_15)

        self.loadobd1btn1 = QPushButton(self.judulOBD_3)
        self.loadobd1btn1.setObjectName(u"loadobd1btn1")
        self.loadobd1btn1.setFont(font4)

        self.horizontalLayout_24.addWidget(self.loadobd1btn1)

        self.horizontalSpacer_14 = QSpacerItem(30, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_14)

        self.loadobd1btn2 = QPushButton(self.judulOBD_3)
        self.loadobd1btn2.setObjectName(u"loadobd1btn2")
        self.loadobd1btn2.setFont(font4)

        self.horizontalLayout_24.addWidget(self.loadobd1btn2)


        self.verticalLayout_15.addWidget(self.judulOBD_3)

        self.widget_2 = QWidget(self.LoadOBD)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy2.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy2)
        self.verticalLayout_37 = QVBoxLayout(self.widget_2)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)
        self.label_5.setLayoutDirection(Qt.LeftToRight)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_37.addWidget(self.label_5)


        self.verticalLayout_15.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.LoadOBD)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy5.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy5)
        self.widget_3.setMinimumSize(QSize(0, 0))
        self.widget_3.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_25 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")
        font5 = QFont()
        font5.setPointSize(16)
        self.label_4.setFont(font5)

        self.horizontalLayout_25.addWidget(self.label_4)

        self.OBDfilebrowse = QLineEdit(self.widget_3)
        self.OBDfilebrowse.setObjectName(u"OBDfilebrowse")
        self.OBDfilebrowse.setMaximumSize(QSize(16777215, 30))
        font6 = QFont()
        font6.setPointSize(13)
        font6.setItalic(True)
        self.OBDfilebrowse.setFont(font6)

        self.horizontalLayout_25.addWidget(self.OBDfilebrowse)

        self.showDataOBDcsv = QPushButton(self.widget_3)
        self.showDataOBDcsv.setObjectName(u"showDataOBDcsv")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/arrow-right-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.showDataOBDcsv.setIcon(icon7)
        self.showDataOBDcsv.setIconSize(QSize(50, 30))

        self.horizontalLayout_25.addWidget(self.showDataOBDcsv, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.obdfilebtn = QPushButton(self.widget_3)
        self.obdfilebtn.setObjectName(u"obdfilebtn")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/more-horizontal.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.obdfilebtn.setIcon(icon8)
        self.obdfilebtn.setIconSize(QSize(30, 30))

        self.horizontalLayout_25.addWidget(self.obdfilebtn)


        self.verticalLayout_15.addWidget(self.widget_3)

        self.obdPages.addWidget(self.LoadOBD)
        self.obd1 = QWidget()
        self.obd1.setObjectName(u"obd1")
        self.verticalLayout_38 = QVBoxLayout(self.obd1)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.judulOBD = QWidget(self.obd1)
        self.judulOBD.setObjectName(u"judulOBD")
        self.horizontalLayout_16 = QHBoxLayout(self.judulOBD)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(20, 0, 20, 0)
        self.Judul = QLabel(self.judulOBD)
        self.Judul.setObjectName(u"Judul")
        self.Judul.setFont(font3)

        self.horizontalLayout_16.addWidget(self.Judul)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_8)

        self.LoadFileOBD1 = QPushButton(self.judulOBD)
        self.LoadFileOBD1.setObjectName(u"LoadFileOBD1")
        self.LoadFileOBD1.setFont(font4)

        self.horizontalLayout_16.addWidget(self.LoadFileOBD1)

        self.horizontalSpacer_6 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_6)

        self.obd1btn1 = QPushButton(self.judulOBD)
        self.obd1btn1.setObjectName(u"obd1btn1")
        self.obd1btn1.setFont(font4)

        self.horizontalLayout_16.addWidget(self.obd1btn1)

        self.horizontalSpacer_9 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_9)

        self.obd1btn2 = QPushButton(self.judulOBD)
        self.obd1btn2.setObjectName(u"obd1btn2")
        self.obd1btn2.setFont(font4)

        self.horizontalLayout_16.addWidget(self.obd1btn2)


        self.verticalLayout_38.addWidget(self.judulOBD)

        self.content_obd = QWidget(self.obd1)
        self.content_obd.setObjectName(u"content_obd")
        sizePolicy3.setHeightForWidth(self.content_obd.sizePolicy().hasHeightForWidth())
        self.content_obd.setSizePolicy(sizePolicy3)
        self.horizontalLayout_18 = QHBoxLayout(self.content_obd)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.content_obd)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_16 = QVBoxLayout(self.widget_4)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.rpmChart = QChartView(self.widget_4)
        self.rpmChart.setObjectName(u"rpmChart")

        self.verticalLayout_16.addWidget(self.rpmChart)

        self.coolantChart = QChartView(self.widget_4)
        self.coolantChart.setObjectName(u"coolantChart")

        self.verticalLayout_16.addWidget(self.coolantChart)

        self.olitempChart = QChartView(self.widget_4)
        self.olitempChart.setObjectName(u"olitempChart")

        self.verticalLayout_16.addWidget(self.olitempChart)


        self.horizontalLayout_18.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.content_obd)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_21 = QVBoxLayout(self.widget_5)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.obdData1 = QTableWidget(self.widget_5)
        if (self.obdData1.columnCount() < 3):
            self.obdData1.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font4);
        self.obdData1.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font4);
        self.obdData1.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font4);
        self.obdData1.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.obdData1.setObjectName(u"obdData1")
        sizePolicy.setHeightForWidth(self.obdData1.sizePolicy().hasHeightForWidth())
        self.obdData1.setSizePolicy(sizePolicy)
        self.obdData1.setMinimumSize(QSize(0, 370))
        self.obdData1.setMaximumSize(QSize(16777215, 450))
        self.obdData1.setSizeIncrement(QSize(926, 0))
        font7 = QFont()
        font7.setFamilies([u"Sans Serif Collection"])
        font7.setPointSize(10)
        font7.setBold(False)
        self.obdData1.setFont(font7)
        self.obdData1.setFocusPolicy(Qt.NoFocus)
        self.obdData1.setInputMethodHints(Qt.ImhDigitsOnly)
        self.obdData1.setAutoScrollMargin(10)
        self.obdData1.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.obdData1.setAlternatingRowColors(False)
        self.obdData1.horizontalHeader().setDefaultSectionSize(70)

        self.verticalLayout_21.addWidget(self.obdData1)


        self.horizontalLayout_18.addWidget(self.widget_5, 0, Qt.AlignRight)


        self.verticalLayout_38.addWidget(self.content_obd)

        self.obdPages.addWidget(self.obd1)
        self.obd2 = QWidget()
        self.obd2.setObjectName(u"obd2")
        self.verticalLayout_39 = QVBoxLayout(self.obd2)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.judulOBD_2 = QWidget(self.obd2)
        self.judulOBD_2.setObjectName(u"judulOBD_2")
        self.horizontalLayout_20 = QHBoxLayout(self.judulOBD_2)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(20, 0, 20, 0)
        self.Judul_2 = QLabel(self.judulOBD_2)
        self.Judul_2.setObjectName(u"Judul_2")
        self.Judul_2.setFont(font3)

        self.horizontalLayout_20.addWidget(self.Judul_2)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_10)

        self.LoadFileOBD2 = QPushButton(self.judulOBD_2)
        self.LoadFileOBD2.setObjectName(u"LoadFileOBD2")
        self.LoadFileOBD2.setFont(font4)

        self.horizontalLayout_20.addWidget(self.LoadFileOBD2)

        self.horizontalSpacer_7 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_7)

        self.obd2btn1 = QPushButton(self.judulOBD_2)
        self.obd2btn1.setObjectName(u"obd2btn1")
        self.obd2btn1.setFont(font4)

        self.horizontalLayout_20.addWidget(self.obd2btn1)

        self.horizontalSpacer_11 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_11)

        self.obd2btn2 = QPushButton(self.judulOBD_2)
        self.obd2btn2.setObjectName(u"obd2btn2")
        self.obd2btn2.setFont(font4)

        self.horizontalLayout_20.addWidget(self.obd2btn2)


        self.verticalLayout_39.addWidget(self.judulOBD_2)

        self.content_obd_2 = QWidget(self.obd2)
        self.content_obd_2.setObjectName(u"content_obd_2")
        sizePolicy3.setHeightForWidth(self.content_obd_2.sizePolicy().hasHeightForWidth())
        self.content_obd_2.setSizePolicy(sizePolicy3)
        self.horizontalLayout_19 = QHBoxLayout(self.content_obd_2)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.content_obd_2)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_22 = QVBoxLayout(self.widget_6)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.speedChart = QChartView(self.widget_6)
        self.speedChart.setObjectName(u"speedChart")

        self.verticalLayout_22.addWidget(self.speedChart)

        self.throttleChart = QChartView(self.widget_6)
        self.throttleChart.setObjectName(u"throttleChart")

        self.verticalLayout_22.addWidget(self.throttleChart)


        self.horizontalLayout_19.addWidget(self.widget_6)

        self.widget_7 = QWidget(self.content_obd_2)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy6)
        self.widget_7.setMaximumSize(QSize(220, 16777215))
        self.verticalLayout_23 = QVBoxLayout(self.widget_7)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(10, 0, 5, 0)
        self.obdData2 = QTableWidget(self.widget_7)
        if (self.obdData2.columnCount() < 2):
            self.obdData2.setColumnCount(2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font4);
        self.obdData2.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font4);
        self.obdData2.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        self.obdData2.setObjectName(u"obdData2")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.obdData2.sizePolicy().hasHeightForWidth())
        self.obdData2.setSizePolicy(sizePolicy7)
        self.obdData2.setMinimumSize(QSize(0, 370))
        self.obdData2.setMaximumSize(QSize(16777215, 450))
        self.obdData2.setSizeIncrement(QSize(926, 0))
        self.obdData2.setFont(font7)
        self.obdData2.setFocusPolicy(Qt.NoFocus)
        self.obdData2.setInputMethodHints(Qt.ImhDigitsOnly)
        self.obdData2.setAutoScrollMargin(10)
        self.obdData2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.obdData2.setAlternatingRowColors(False)
        self.obdData2.horizontalHeader().setDefaultSectionSize(80)

        self.verticalLayout_23.addWidget(self.obdData2)


        self.horizontalLayout_19.addWidget(self.widget_7, 0, Qt.AlignRight)


        self.verticalLayout_39.addWidget(self.content_obd_2)

        self.obdPages.addWidget(self.obd2)

        self.verticalLayout_9.addWidget(self.obdPages)

        self.mainPages.addWidget(self.obdPage)
        self.imuPage = QWidget()
        self.imuPage.setObjectName(u"imuPage")
        self.verticalLayout_10 = QVBoxLayout(self.imuPage)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.imuPages = QStackedWidget(self.imuPage)
        self.imuPages.setObjectName(u"imuPages")
        self.LoadIMU = QWidget()
        self.LoadIMU.setObjectName(u"LoadIMU")
        self.verticalLayout_12 = QVBoxLayout(self.LoadIMU)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.LoadIMU)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy)
        self.frame_13.setMaximumSize(QSize(16777215, 40))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(20, 0, 20, 0)
        self.label_14 = QLabel(self.frame_13)
        self.label_14.setObjectName(u"label_14")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy8)
        self.label_14.setFont(font3)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_26.addWidget(self.label_14)

        self.horizontalSpacer_16 = QSpacerItem(20, 24, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_16)

        self.BLoadFileInertial = QPushButton(self.frame_13)
        self.BLoadFileInertial.setObjectName(u"BLoadFileInertial")
        self.BLoadFileInertial.setFont(font4)

        self.horizontalLayout_26.addWidget(self.BLoadFileInertial)

        self.horizontalSpacer_41 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_41)

        self.BImpact = QPushButton(self.frame_13)
        self.BImpact.setObjectName(u"BImpact")
        self.BImpact.setFont(font4)

        self.horizontalLayout_26.addWidget(self.BImpact)

        self.horizontalSpacer_42 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_42)

        self.BRawDatabtn = QPushButton(self.frame_13)
        self.BRawDatabtn.setObjectName(u"BRawDatabtn")
        self.BRawDatabtn.setFont(font4)

        self.horizontalLayout_26.addWidget(self.BRawDatabtn)

        self.horizontalSpacer_43 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_43)

        self.BQuaternionbtn = QPushButton(self.frame_13)
        self.BQuaternionbtn.setObjectName(u"BQuaternionbtn")
        self.BQuaternionbtn.setFont(font4)

        self.horizontalLayout_26.addWidget(self.BQuaternionbtn)

        self.horizontalSpacer_44 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_44)

        self.BEulerbtn = QPushButton(self.frame_13)
        self.BEulerbtn.setObjectName(u"BEulerbtn")
        self.BEulerbtn.setFont(font4)

        self.horizontalLayout_26.addWidget(self.BEulerbtn)

        self.horizontalSpacer_45 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_45)

        self.BSimulationbtn = QPushButton(self.frame_13)
        self.BSimulationbtn.setObjectName(u"BSimulationbtn")
        self.BSimulationbtn.setFont(font4)

        self.horizontalLayout_26.addWidget(self.BSimulationbtn)


        self.verticalLayout_12.addWidget(self.frame_13)

        self.widget_8 = QWidget(self.LoadIMU)
        self.widget_8.setObjectName(u"widget_8")
        sizePolicy1.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy1)
        self.verticalLayout_17 = QVBoxLayout(self.widget_8)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.widget_8)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font2)
        self.label_16.setLayoutDirection(Qt.LeftToRight)
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_16)


        self.verticalLayout_12.addWidget(self.widget_8)

        self.widget_9 = QWidget(self.LoadIMU)
        self.widget_9.setObjectName(u"widget_9")
        sizePolicy.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy)
        self.widget_9.setMinimumSize(QSize(0, 0))
        self.widget_9.setMaximumSize(QSize(16777215, 200))
        self.gridLayout_2 = QGridLayout(self.widget_9)
        self.gridLayout_2.setSpacing(9)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(20, 0, 20, 9)
        self.rawinerfilebtn = QPushButton(self.widget_9)
        self.rawinerfilebtn.setObjectName(u"rawinerfilebtn")
        self.rawinerfilebtn.setIcon(icon8)
        self.rawinerfilebtn.setIconSize(QSize(25, 25))

        self.gridLayout_2.addWidget(self.rawinerfilebtn, 1, 5, 1, 2)

        self.quaternionfilebtn = QPushButton(self.widget_9)
        self.quaternionfilebtn.setObjectName(u"quaternionfilebtn")
        self.quaternionfilebtn.setIcon(icon8)
        self.quaternionfilebtn.setIconSize(QSize(25, 25))

        self.gridLayout_2.addWidget(self.quaternionfilebtn, 2, 5, 1, 2)

        self.label_23 = QLabel(self.widget_9)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font5)

        self.gridLayout_2.addWidget(self.label_23, 3, 0, 1, 2)

        self.label_20 = QLabel(self.widget_9)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font5)

        self.gridLayout_2.addWidget(self.label_20, 0, 0, 1, 1)

        self.label_22 = QLabel(self.widget_9)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font5)

        self.gridLayout_2.addWidget(self.label_22, 2, 0, 1, 3)

        self.eulerfilebtn = QPushButton(self.widget_9)
        self.eulerfilebtn.setObjectName(u"eulerfilebtn")
        self.eulerfilebtn.setIcon(icon8)
        self.eulerfilebtn.setIconSize(QSize(25, 25))

        self.gridLayout_2.addWidget(self.eulerfilebtn, 3, 5, 1, 2)

        self.label_21 = QLabel(self.widget_9)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font5)

        self.gridLayout_2.addWidget(self.label_21, 1, 0, 1, 2)

        self.rawinerupBtn = QPushButton(self.widget_9)
        self.rawinerupBtn.setObjectName(u"rawinerupBtn")
        self.rawinerupBtn.setIcon(icon7)
        self.rawinerupBtn.setIconSize(QSize(25, 25))

        self.gridLayout_2.addWidget(self.rawinerupBtn, 1, 4, 1, 1)

        self.eulerupBtn = QPushButton(self.widget_9)
        self.eulerupBtn.setObjectName(u"eulerupBtn")
        self.eulerupBtn.setIcon(icon7)
        self.eulerupBtn.setIconSize(QSize(25, 25))

        self.gridLayout_2.addWidget(self.eulerupBtn, 3, 4, 1, 1)

        self.quaternionupBtn = QPushButton(self.widget_9)
        self.quaternionupBtn.setObjectName(u"quaternionupBtn")
        self.quaternionupBtn.setIcon(icon7)
        self.quaternionupBtn.setIconSize(QSize(25, 25))

        self.gridLayout_2.addWidget(self.quaternionupBtn, 2, 4, 1, 1)

        self.impactupBtn = QPushButton(self.widget_9)
        self.impactupBtn.setObjectName(u"impactupBtn")
        self.impactupBtn.setIcon(icon7)
        self.impactupBtn.setIconSize(QSize(25, 25))

        self.gridLayout_2.addWidget(self.impactupBtn, 0, 4, 1, 1)

        self.impactfilebrowse = QLineEdit(self.widget_9)
        self.impactfilebrowse.setObjectName(u"impactfilebrowse")
        sizePolicy9 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.impactfilebrowse.sizePolicy().hasHeightForWidth())
        self.impactfilebrowse.setSizePolicy(sizePolicy9)
        self.impactfilebrowse.setMaximumSize(QSize(16777215, 30))
        font8 = QFont()
        font8.setPointSize(12)
        font8.setItalic(True)
        self.impactfilebrowse.setFont(font8)

        self.gridLayout_2.addWidget(self.impactfilebrowse, 0, 3, 1, 1)

        self.rawinerfilebrowse = QLineEdit(self.widget_9)
        self.rawinerfilebrowse.setObjectName(u"rawinerfilebrowse")
        self.rawinerfilebrowse.setMaximumSize(QSize(16777215, 30))
        self.rawinerfilebrowse.setFont(font8)

        self.gridLayout_2.addWidget(self.rawinerfilebrowse, 1, 3, 1, 1)

        self.quaternionfilebrowse = QLineEdit(self.widget_9)
        self.quaternionfilebrowse.setObjectName(u"quaternionfilebrowse")
        self.quaternionfilebrowse.setMaximumSize(QSize(16777215, 30))
        self.quaternionfilebrowse.setFont(font8)

        self.gridLayout_2.addWidget(self.quaternionfilebrowse, 2, 3, 1, 1)

        self.eulerfilebrowse = QLineEdit(self.widget_9)
        self.eulerfilebrowse.setObjectName(u"eulerfilebrowse")
        self.eulerfilebrowse.setMaximumSize(QSize(16777215, 30))
        self.eulerfilebrowse.setFont(font8)

        self.gridLayout_2.addWidget(self.eulerfilebrowse, 3, 3, 1, 1)

        self.impactfilebtn = QPushButton(self.widget_9)
        self.impactfilebtn.setObjectName(u"impactfilebtn")
        self.impactfilebtn.setIcon(icon8)
        self.impactfilebtn.setIconSize(QSize(25, 25))

        self.gridLayout_2.addWidget(self.impactfilebtn, 0, 5, 1, 1)


        self.verticalLayout_12.addWidget(self.widget_9)

        self.imuPages.addWidget(self.LoadIMU)
        self.ImpactPage = QWidget()
        self.ImpactPage.setObjectName(u"ImpactPage")
        self.verticalLayout_20 = QVBoxLayout(self.ImpactPage)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.ImpactPage)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setMaximumSize(QSize(16777215, 40))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(20, 0, 20, 0)
        self.label_12 = QLabel(self.frame_10)
        self.label_12.setObjectName(u"label_12")
        sizePolicy8.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy8)
        self.label_12.setFont(font3)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.label_12)

        self.horizontalSpacer_12 = QSpacerItem(300, 30, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_12)

        self.FLoadFileInertial = QPushButton(self.frame_10)
        self.FLoadFileInertial.setObjectName(u"FLoadFileInertial")
        self.FLoadFileInertial.setFont(font4)

        self.horizontalLayout_23.addWidget(self.FLoadFileInertial)

        self.horizontalSpacer_36 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_36)

        self.FImpact = QPushButton(self.frame_10)
        self.FImpact.setObjectName(u"FImpact")
        self.FImpact.setFont(font4)

        self.horizontalLayout_23.addWidget(self.FImpact)

        self.horizontalSpacer_37 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_37)

        self.FRawDatabtn = QPushButton(self.frame_10)
        self.FRawDatabtn.setObjectName(u"FRawDatabtn")
        self.FRawDatabtn.setFont(font4)

        self.horizontalLayout_23.addWidget(self.FRawDatabtn)

        self.horizontalSpacer_38 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_38)

        self.FQuaternionbtn = QPushButton(self.frame_10)
        self.FQuaternionbtn.setObjectName(u"FQuaternionbtn")
        self.FQuaternionbtn.setFont(font4)

        self.horizontalLayout_23.addWidget(self.FQuaternionbtn)

        self.horizontalSpacer_39 = QSpacerItem(30, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_39)

        self.FEulerbtn = QPushButton(self.frame_10)
        self.FEulerbtn.setObjectName(u"FEulerbtn")
        self.FEulerbtn.setFont(font4)

        self.horizontalLayout_23.addWidget(self.FEulerbtn)

        self.horizontalSpacer_40 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_40)

        self.FSimulationbtn = QPushButton(self.frame_10)
        self.FSimulationbtn.setObjectName(u"FSimulationbtn")
        self.FSimulationbtn.setFont(font4)

        self.horizontalLayout_23.addWidget(self.FSimulationbtn)


        self.verticalLayout_20.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.ImpactPage)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy3.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy3)
        self.frame_11.setMinimumSize(QSize(0, 220))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_11)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.ImpactChart = QChartView(self.frame_11)
        self.ImpactChart.setObjectName(u"ImpactChart")

        self.verticalLayout_26.addWidget(self.ImpactChart)

        self.ImpactTable = QTableWidget(self.frame_11)
        if (self.ImpactTable.columnCount() < 3):
            self.ImpactTable.setColumnCount(3)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font4);
        self.ImpactTable.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font4);
        self.ImpactTable.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font4);
        self.ImpactTable.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        self.ImpactTable.setObjectName(u"ImpactTable")
        sizePolicy.setHeightForWidth(self.ImpactTable.sizePolicy().hasHeightForWidth())
        self.ImpactTable.setSizePolicy(sizePolicy)
        self.ImpactTable.setMinimumSize(QSize(0, 0))
        self.ImpactTable.setMaximumSize(QSize(16777215, 300))
        self.ImpactTable.setSizeIncrement(QSize(927, 0))
        self.ImpactTable.setFont(font7)
        self.ImpactTable.setFocusPolicy(Qt.NoFocus)
        self.ImpactTable.setInputMethodHints(Qt.ImhDigitsOnly)
        self.ImpactTable.setAutoScrollMargin(10)
        self.ImpactTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ImpactTable.setAlternatingRowColors(False)
        self.ImpactTable.horizontalHeader().setDefaultSectionSize(300)

        self.verticalLayout_26.addWidget(self.ImpactTable)


        self.verticalLayout_20.addWidget(self.frame_11)

        self.imuPages.addWidget(self.ImpactPage)
        self.rawDataIMU = QWidget()
        self.rawDataIMU.setObjectName(u"rawDataIMU")
        self.verticalLayout_30 = QVBoxLayout(self.rawDataIMU)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.rawDataIMU)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setMaximumSize(QSize(16777215, 40))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(20, 0, 20, 0)
        self.label_11 = QLabel(self.frame_9)
        self.label_11.setObjectName(u"label_11")
        sizePolicy8.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy8)
        self.label_11.setFont(font3)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_11)

        self.horizontalSpacer_2 = QSpacerItem(20, 24, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.iLoadFileInertial = QPushButton(self.frame_9)
        self.iLoadFileInertial.setObjectName(u"iLoadFileInertial")
        self.iLoadFileInertial.setFont(font4)

        self.horizontalLayout_3.addWidget(self.iLoadFileInertial)

        self.horizontalSpacer_31 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_31)

        self.iImpact = QPushButton(self.frame_9)
        self.iImpact.setObjectName(u"iImpact")
        self.iImpact.setFont(font4)

        self.horizontalLayout_3.addWidget(self.iImpact)

        self.horizontalSpacer_32 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_32)

        self.iRawDatabtn = QPushButton(self.frame_9)
        self.iRawDatabtn.setObjectName(u"iRawDatabtn")
        self.iRawDatabtn.setFont(font4)

        self.horizontalLayout_3.addWidget(self.iRawDatabtn)

        self.horizontalSpacer_33 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_33)

        self.iQuaternionbtn = QPushButton(self.frame_9)
        self.iQuaternionbtn.setObjectName(u"iQuaternionbtn")
        self.iQuaternionbtn.setFont(font4)

        self.horizontalLayout_3.addWidget(self.iQuaternionbtn)

        self.horizontalSpacer_34 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_34)

        self.iEulerbtn = QPushButton(self.frame_9)
        self.iEulerbtn.setObjectName(u"iEulerbtn")
        self.iEulerbtn.setFont(font4)

        self.horizontalLayout_3.addWidget(self.iEulerbtn)

        self.horizontalSpacer_35 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_35)

        self.iSimulationbtn = QPushButton(self.frame_9)
        self.iSimulationbtn.setObjectName(u"iSimulationbtn")
        self.iSimulationbtn.setFont(font4)

        self.horizontalLayout_3.addWidget(self.iSimulationbtn)


        self.verticalLayout_30.addWidget(self.frame_9)

        self.frame_8 = QFrame(self.rawDataIMU)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy3.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy3)
        self.frame_8.setMinimumSize(QSize(0, 220))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_8)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.ImuChart = QChartView(self.frame_8)
        self.ImuChart.setObjectName(u"ImuChart")

        self.verticalLayout_19.addWidget(self.ImuChart)

        self.inertialTable = QTableWidget(self.frame_8)
        if (self.inertialTable.columnCount() < 9):
            self.inertialTable.setColumnCount(9)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font4);
        self.inertialTable.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font4);
        self.inertialTable.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font4);
        self.inertialTable.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font4);
        self.inertialTable.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font4);
        self.inertialTable.setHorizontalHeaderItem(4, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font4);
        self.inertialTable.setHorizontalHeaderItem(5, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font4);
        self.inertialTable.setHorizontalHeaderItem(6, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font4);
        self.inertialTable.setHorizontalHeaderItem(7, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setFont(font4);
        self.inertialTable.setHorizontalHeaderItem(8, __qtablewidgetitem16)
        self.inertialTable.setObjectName(u"inertialTable")
        sizePolicy.setHeightForWidth(self.inertialTable.sizePolicy().hasHeightForWidth())
        self.inertialTable.setSizePolicy(sizePolicy)
        self.inertialTable.setMinimumSize(QSize(0, 0))
        self.inertialTable.setMaximumSize(QSize(16777215, 300))
        self.inertialTable.setSizeIncrement(QSize(927, 0))
        self.inertialTable.setFont(font7)
        self.inertialTable.setFocusPolicy(Qt.NoFocus)
        self.inertialTable.setInputMethodHints(Qt.ImhDigitsOnly)
        self.inertialTable.setAutoScrollMargin(10)
        self.inertialTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.inertialTable.setAlternatingRowColors(False)
        self.inertialTable.horizontalHeader().setDefaultSectionSize(100)

        self.verticalLayout_19.addWidget(self.inertialTable)


        self.verticalLayout_30.addWidget(self.frame_8)

        self.imuPages.addWidget(self.rawDataIMU)
        self.quaternion = QWidget()
        self.quaternion.setObjectName(u"quaternion")
        self.verticalLayout_32 = QVBoxLayout(self.quaternion)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.quaternion)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy)
        self.frame_15.setMaximumSize(QSize(16777215, 40))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(20, 0, 20, 0)
        self.label_13 = QLabel(self.frame_15)
        self.label_13.setObjectName(u"label_13")
        sizePolicy8.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy8)
        self.label_13.setFont(font3)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_13)

        self.horizontalSpacer_3 = QSpacerItem(20, 24, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.qLoadFileInertial = QPushButton(self.frame_15)
        self.qLoadFileInertial.setObjectName(u"qLoadFileInertial")
        self.qLoadFileInertial.setFont(font4)

        self.horizontalLayout_6.addWidget(self.qLoadFileInertial)

        self.horizontalSpacer_26 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_26)

        self.qImpact = QPushButton(self.frame_15)
        self.qImpact.setObjectName(u"qImpact")
        self.qImpact.setFont(font4)

        self.horizontalLayout_6.addWidget(self.qImpact)

        self.horizontalSpacer_27 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_27)

        self.qRawDatabtn = QPushButton(self.frame_15)
        self.qRawDatabtn.setObjectName(u"qRawDatabtn")
        self.qRawDatabtn.setFont(font4)

        self.horizontalLayout_6.addWidget(self.qRawDatabtn)

        self.horizontalSpacer_28 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_28)

        self.qQuaternionbtn = QPushButton(self.frame_15)
        self.qQuaternionbtn.setObjectName(u"qQuaternionbtn")
        self.qQuaternionbtn.setFont(font4)

        self.horizontalLayout_6.addWidget(self.qQuaternionbtn)

        self.horizontalSpacer_29 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_29)

        self.qEulerbtn = QPushButton(self.frame_15)
        self.qEulerbtn.setObjectName(u"qEulerbtn")
        self.qEulerbtn.setFont(font4)

        self.horizontalLayout_6.addWidget(self.qEulerbtn)

        self.horizontalSpacer_30 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_30)

        self.qSimulationbtn = QPushButton(self.frame_15)
        self.qSimulationbtn.setObjectName(u"qSimulationbtn")
        self.qSimulationbtn.setFont(font4)

        self.horizontalLayout_6.addWidget(self.qSimulationbtn)


        self.verticalLayout_32.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.quaternion)
        self.frame_16.setObjectName(u"frame_16")
        sizePolicy3.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy3)
        self.frame_16.setMinimumSize(QSize(0, 220))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_16)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.quaternionChart = QChartView(self.frame_16)
        self.quaternionChart.setObjectName(u"quaternionChart")

        self.verticalLayout_35.addWidget(self.quaternionChart)


        self.verticalLayout_32.addWidget(self.frame_16)

        self.frame_14 = QFrame(self.quaternion)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy3.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy3)
        self.frame_14.setMinimumSize(QSize(0, 220))
        self.frame_14.setMaximumSize(QSize(16777215, 300))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_14)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.quaternionTable = QTableWidget(self.frame_14)
        if (self.quaternionTable.columnCount() < 4):
            self.quaternionTable.setColumnCount(4)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setFont(font4);
        self.quaternionTable.setHorizontalHeaderItem(0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setFont(font4);
        self.quaternionTable.setHorizontalHeaderItem(1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setFont(font4);
        self.quaternionTable.setHorizontalHeaderItem(2, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setFont(font4);
        self.quaternionTable.setHorizontalHeaderItem(3, __qtablewidgetitem20)
        self.quaternionTable.setObjectName(u"quaternionTable")
        sizePolicy3.setHeightForWidth(self.quaternionTable.sizePolicy().hasHeightForWidth())
        self.quaternionTable.setSizePolicy(sizePolicy3)
        self.quaternionTable.setMinimumSize(QSize(0, 0))
        self.quaternionTable.setMaximumSize(QSize(16777215, 300))
        self.quaternionTable.setSizeIncrement(QSize(927, 0))
        self.quaternionTable.setFont(font7)
        self.quaternionTable.setFocusPolicy(Qt.NoFocus)
        self.quaternionTable.setInputMethodHints(Qt.ImhDigitsOnly)
        self.quaternionTable.setAutoScrollMargin(10)
        self.quaternionTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.quaternionTable.setAlternatingRowColors(False)
        self.quaternionTable.horizontalHeader().setDefaultSectionSize(220)

        self.verticalLayout_29.addWidget(self.quaternionTable)


        self.verticalLayout_32.addWidget(self.frame_14)

        self.imuPages.addWidget(self.quaternion)
        self.eulerAngle = QWidget()
        self.eulerAngle.setObjectName(u"eulerAngle")
        self.verticalLayout_40 = QVBoxLayout(self.eulerAngle)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.eulerAngle)
        self.frame_17.setObjectName(u"frame_17")
        sizePolicy.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy)
        self.frame_17.setMaximumSize(QSize(16777215, 40))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(20, 0, 20, 0)
        self.label_15 = QLabel(self.frame_17)
        self.label_15.setObjectName(u"label_15")
        sizePolicy8.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy8)
        self.label_15.setFont(font3)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_15)

        self.horizontalSpacer_4 = QSpacerItem(20, 24, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_4)

        self.eLoadFileInertial = QPushButton(self.frame_17)
        self.eLoadFileInertial.setObjectName(u"eLoadFileInertial")
        self.eLoadFileInertial.setFont(font4)

        self.horizontalLayout_13.addWidget(self.eLoadFileInertial)

        self.horizontalSpacer_46 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_46)

        self.eImpact = QPushButton(self.frame_17)
        self.eImpact.setObjectName(u"eImpact")
        self.eImpact.setFont(font4)

        self.horizontalLayout_13.addWidget(self.eImpact)

        self.horizontalSpacer_22 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_22)

        self.eRawDatabtn = QPushButton(self.frame_17)
        self.eRawDatabtn.setObjectName(u"eRawDatabtn")
        self.eRawDatabtn.setFont(font4)

        self.horizontalLayout_13.addWidget(self.eRawDatabtn)

        self.horizontalSpacer_23 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_23)

        self.eQuaternionbtn = QPushButton(self.frame_17)
        self.eQuaternionbtn.setObjectName(u"eQuaternionbtn")
        self.eQuaternionbtn.setFont(font4)

        self.horizontalLayout_13.addWidget(self.eQuaternionbtn)

        self.horizontalSpacer_24 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_24)

        self.eEulerbtn = QPushButton(self.frame_17)
        self.eEulerbtn.setObjectName(u"eEulerbtn")
        self.eEulerbtn.setFont(font4)

        self.horizontalLayout_13.addWidget(self.eEulerbtn)

        self.horizontalSpacer_25 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_25)

        self.eSimulationbtn = QPushButton(self.frame_17)
        self.eSimulationbtn.setObjectName(u"eSimulationbtn")
        self.eSimulationbtn.setFont(font4)

        self.horizontalLayout_13.addWidget(self.eSimulationbtn)


        self.verticalLayout_40.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.eulerAngle)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy3.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy3)
        self.frame_18.setMinimumSize(QSize(0, 220))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_18)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.EulerChart = QChartView(self.frame_18)
        self.EulerChart.setObjectName(u"EulerChart")
        self.EulerChart.setLineWidth(0)

        self.verticalLayout_36.addWidget(self.EulerChart)


        self.verticalLayout_40.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.eulerAngle)
        self.frame_19.setObjectName(u"frame_19")
        sizePolicy.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy)
        self.frame_19.setMinimumSize(QSize(0, 220))
        self.frame_19.setMaximumSize(QSize(16777215, 300))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_19)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.eulerTable = QTableWidget(self.frame_19)
        if (self.eulerTable.columnCount() < 3):
            self.eulerTable.setColumnCount(3)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setFont(font4);
        self.eulerTable.setHorizontalHeaderItem(0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setFont(font4);
        self.eulerTable.setHorizontalHeaderItem(1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setFont(font4);
        self.eulerTable.setHorizontalHeaderItem(2, __qtablewidgetitem23)
        self.eulerTable.setObjectName(u"eulerTable")
        sizePolicy3.setHeightForWidth(self.eulerTable.sizePolicy().hasHeightForWidth())
        self.eulerTable.setSizePolicy(sizePolicy3)
        self.eulerTable.setMinimumSize(QSize(0, 0))
        self.eulerTable.setMaximumSize(QSize(16777215, 300))
        self.eulerTable.setSizeIncrement(QSize(927, 0))
        self.eulerTable.setFont(font7)
        self.eulerTable.setFocusPolicy(Qt.NoFocus)
        self.eulerTable.setInputMethodHints(Qt.ImhDigitsOnly)
        self.eulerTable.setAutoScrollMargin(10)
        self.eulerTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.eulerTable.setAlternatingRowColors(False)
        self.eulerTable.horizontalHeader().setDefaultSectionSize(300)

        self.verticalLayout_31.addWidget(self.eulerTable)


        self.verticalLayout_40.addWidget(self.frame_19)

        self.imuPages.addWidget(self.eulerAngle)
        self.simulation = QWidget()
        self.simulation.setObjectName(u"simulation")
        self.verticalLayout_41 = QVBoxLayout(self.simulation)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.simulation)
        self.frame_20.setObjectName(u"frame_20")
        sizePolicy.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy)
        self.frame_20.setMaximumSize(QSize(16777215, 40))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(20, 0, 20, 0)
        self.label_17 = QLabel(self.frame_20)
        self.label_17.setObjectName(u"label_17")
        sizePolicy1.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy1)
        self.label_17.setFont(font3)
        self.label_17.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_17)

        self.horizontalSpacer_5 = QSpacerItem(20, 24, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_5)

        self.sLoadFileInertial = QPushButton(self.frame_20)
        self.sLoadFileInertial.setObjectName(u"sLoadFileInertial")
        self.sLoadFileInertial.setFont(font4)

        self.horizontalLayout_14.addWidget(self.sLoadFileInertial)

        self.horizontalSpacer_17 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_17)

        self.sImpact = QPushButton(self.frame_20)
        self.sImpact.setObjectName(u"sImpact")
        self.sImpact.setFont(font4)

        self.horizontalLayout_14.addWidget(self.sImpact)

        self.horizontalSpacer_18 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_18)

        self.sRawDatabtn = QPushButton(self.frame_20)
        self.sRawDatabtn.setObjectName(u"sRawDatabtn")
        self.sRawDatabtn.setFont(font4)

        self.horizontalLayout_14.addWidget(self.sRawDatabtn)

        self.horizontalSpacer_19 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_19)

        self.sQuaternionbtn = QPushButton(self.frame_20)
        self.sQuaternionbtn.setObjectName(u"sQuaternionbtn")
        self.sQuaternionbtn.setFont(font4)

        self.horizontalLayout_14.addWidget(self.sQuaternionbtn)

        self.horizontalSpacer_20 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_20)

        self.sEulerbtn = QPushButton(self.frame_20)
        self.sEulerbtn.setObjectName(u"sEulerbtn")
        self.sEulerbtn.setFont(font4)

        self.horizontalLayout_14.addWidget(self.sEulerbtn)

        self.horizontalSpacer_21 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_21)

        self.sSimulationbtn = QPushButton(self.frame_20)
        self.sSimulationbtn.setObjectName(u"sSimulationbtn")
        self.sSimulationbtn.setFont(font4)

        self.horizontalLayout_14.addWidget(self.sSimulationbtn)


        self.verticalLayout_41.addWidget(self.frame_20)

        self.Simulatio_widget = QWidget(self.simulation)
        self.Simulatio_widget.setObjectName(u"Simulatio_widget")
        sizePolicy1.setHeightForWidth(self.Simulatio_widget.sizePolicy().hasHeightForWidth())
        self.Simulatio_widget.setSizePolicy(sizePolicy1)
        self.Simulatio_widget.setMinimumSize(QSize(0, 0))
        self.verticalLayout_18 = QVBoxLayout(self.Simulatio_widget)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.tittleLayout = QWidget(self.Simulatio_widget)
        self.tittleLayout.setObjectName(u"tittleLayout")
        self.horizontalLayout_4 = QHBoxLayout(self.tittleLayout)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.tittleLayout)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_22)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_18 = QLabel(self.frame_22)
        self.label_18.setObjectName(u"label_18")
        sizePolicy5.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy5)
        self.label_18.setFont(font3)
        self.label_18.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_27.addWidget(self.label_18)


        self.horizontalLayout_4.addWidget(self.frame_22)

        self.frame_24 = QFrame(self.tittleLayout)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_24)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_19 = QLabel(self.frame_24)
        self.label_19.setObjectName(u"label_19")
        sizePolicy5.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy5)
        self.label_19.setFont(font3)
        self.label_19.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_28.addWidget(self.label_19)


        self.horizontalLayout_4.addWidget(self.frame_24)


        self.verticalLayout_18.addWidget(self.tittleLayout)

        self.simulationlayout = QWidget(self.Simulatio_widget)
        self.simulationlayout.setObjectName(u"simulationlayout")
        self.horizontalLayout_15 = QHBoxLayout(self.simulationlayout)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.widgetTrajectory = QWidget(self.simulationlayout)
        self.widgetTrajectory.setObjectName(u"widgetTrajectory")
        sizePolicy3.setHeightForWidth(self.widgetTrajectory.sizePolicy().hasHeightForWidth())
        self.widgetTrajectory.setSizePolicy(sizePolicy3)
        self.verticalLayout_34 = QVBoxLayout(self.widgetTrajectory)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")

        self.horizontalLayout_15.addWidget(self.widgetTrajectory)

        self.widgetOrientaion = QWidget(self.simulationlayout)
        self.widgetOrientaion.setObjectName(u"widgetOrientaion")
        self.verticalLayout_33 = QVBoxLayout(self.widgetOrientaion)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")

        self.horizontalLayout_15.addWidget(self.widgetOrientaion)


        self.verticalLayout_18.addWidget(self.simulationlayout)


        self.verticalLayout_41.addWidget(self.Simulatio_widget)

        self.widget = QWidget(self.simulation)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_11 = QHBoxLayout(self.widget)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.simulationPlay = QPushButton(self.widget)
        self.simulationPlay.setObjectName(u"simulationPlay")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/play-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.simulationPlay.setIcon(icon9)
        self.simulationPlay.setIconSize(QSize(24, 24))

        self.horizontalLayout_11.addWidget(self.simulationPlay)

        self.simulationStop = QPushButton(self.widget)
        self.simulationStop.setObjectName(u"simulationStop")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/stop-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.simulationStop.setIcon(icon10)
        self.simulationStop.setIconSize(QSize(24, 24))

        self.horizontalLayout_11.addWidget(self.simulationStop)


        self.verticalLayout_41.addWidget(self.widget)

        self.imuPages.addWidget(self.simulation)

        self.verticalLayout_10.addWidget(self.imuPages)

        self.mainPages.addWidget(self.imuPage)
        self.gpsPage = QWidget()
        self.gpsPage.setObjectName(u"gpsPage")
        self.gridLayout_3 = QGridLayout(self.gpsPage)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.mapsWidget = QWidget(self.gpsPage)
        self.mapsWidget.setObjectName(u"mapsWidget")
        self.horizontalLayout_22 = QHBoxLayout(self.mapsWidget)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")

        self.gridLayout_3.addWidget(self.mapsWidget, 0, 0, 1, 1)

        self.mapsTable = QWidget(self.gpsPage)
        self.mapsTable.setObjectName(u"mapsTable")
        sizePolicy10 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.mapsTable.sizePolicy().hasHeightForWidth())
        self.mapsTable.setSizePolicy(sizePolicy10)
        self.mapsTable.setMinimumSize(QSize(0, 0))
        self.mapsTable.setMaximumSize(QSize(190, 16777215))
        self.verticalLayout_11 = QVBoxLayout(self.mapsTable)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gpsTable = QTableWidget(self.mapsTable)
        if (self.gpsTable.columnCount() < 2):
            self.gpsTable.setColumnCount(2)
        font9 = QFont()
        font9.setPointSize(10)
        font9.setBold(True)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setFont(font9);
        self.gpsTable.setHorizontalHeaderItem(0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setFont(font9);
        self.gpsTable.setHorizontalHeaderItem(1, __qtablewidgetitem25)
        self.gpsTable.setObjectName(u"gpsTable")
        sizePolicy1.setHeightForWidth(self.gpsTable.sizePolicy().hasHeightForWidth())
        self.gpsTable.setSizePolicy(sizePolicy1)
        self.gpsTable.horizontalHeader().setDefaultSectionSize(90)

        self.verticalLayout_11.addWidget(self.gpsTable)


        self.gridLayout_3.addWidget(self.mapsTable, 0, 1, 1, 1)

        self.widget_10 = QWidget(self.gpsPage)
        self.widget_10.setObjectName(u"widget_10")
        sizePolicy5.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy5)
        self.widget_10.setMinimumSize(QSize(0, 0))
        self.widget_10.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_27 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(20, 0, 20, 0)
        self.label_24 = QLabel(self.widget_10)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font5)

        self.horizontalLayout_27.addWidget(self.label_24)

        self.horizontalSpacer_47 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_47)

        self.gpsfilebrowse = QLineEdit(self.widget_10)
        self.gpsfilebrowse.setObjectName(u"gpsfilebrowse")
        sizePolicy7.setHeightForWidth(self.gpsfilebrowse.sizePolicy().hasHeightForWidth())
        self.gpsfilebrowse.setSizePolicy(sizePolicy7)
        font10 = QFont()
        font10.setPointSize(10)
        font10.setItalic(True)
        self.gpsfilebrowse.setFont(font10)

        self.horizontalLayout_27.addWidget(self.gpsfilebrowse)

        self.horizontalSpacer_48 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_48)

        self.gpsupBtn = QPushButton(self.widget_10)
        self.gpsupBtn.setObjectName(u"gpsupBtn")
        self.gpsupBtn.setIcon(icon7)
        self.gpsupBtn.setIconSize(QSize(25, 25))

        self.horizontalLayout_27.addWidget(self.gpsupBtn)

        self.gpsfilebtn = QPushButton(self.widget_10)
        self.gpsfilebtn.setObjectName(u"gpsfilebtn")
        self.gpsfilebtn.setIcon(icon8)
        self.gpsfilebtn.setIconSize(QSize(25, 25))

        self.horizontalLayout_27.addWidget(self.gpsfilebtn)


        self.gridLayout_3.addWidget(self.widget_10, 1, 0, 1, 2)

        self.mainPages.addWidget(self.gpsPage)
        self.cameraPage = QWidget()
        self.cameraPage.setObjectName(u"cameraPage")
        self.gridLayout = QGridLayout(self.cameraPage)
        self.gridLayout.setObjectName(u"gridLayout")
        self.vCam = QFrame(self.cameraPage)
        self.vCam.setObjectName(u"vCam")
        self.vCam.setMinimumSize(QSize(580, 400))
        self.vCam.setFrameShape(QFrame.StyledPanel)
        self.vCam.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.vCam)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(10, 5, 10, 0)

        self.gridLayout.addWidget(self.vCam, 0, 0, 1, 1)

        self.FERview = QListWidget(self.cameraPage)
        self.FERview.setObjectName(u"FERview")
        sizePolicy11 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.FERview.sizePolicy().hasHeightForWidth())
        self.FERview.setSizePolicy(sizePolicy11)
        self.FERview.setMaximumSize(QSize(150, 400))
        font11 = QFont()
        font11.setPointSize(12)
        font11.setBold(True)
        font11.setItalic(True)
        self.FERview.setFont(font11)
        self.FERview.setAutoScroll(True)
        self.FERview.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.gridLayout.addWidget(self.FERview, 0, 1, 1, 1)

        self.frame_12 = QFrame(self.cameraPage)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy8.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy8)
        self.frame_12.setMinimumSize(QSize(0, 0))
        self.frame_12.setMaximumSize(QSize(16777215, 30))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.widget_11 = QWidget(self.frame_12)
        self.widget_11.setObjectName(u"widget_11")
        sizePolicy12 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.widget_11.sizePolicy().hasHeightForWidth())
        self.widget_11.setSizePolicy(sizePolicy12)
        self.widget_11.setMinimumSize(QSize(700, 0))
        self.widget_11.setMaximumSize(QSize(0, 30))
        self.horizontalLayout_28 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.widget_11)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font5)

        self.horizontalLayout_28.addWidget(self.label_7)

        self.horizontalSpacer_49 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_49)

        self.camerafilebrowse = QLineEdit(self.widget_11)
        self.camerafilebrowse.setObjectName(u"camerafilebrowse")
        self.camerafilebrowse.setMaximumSize(QSize(16777215, 30))
        self.camerafilebrowse.setFont(font8)

        self.horizontalLayout_28.addWidget(self.camerafilebrowse)

        self.horizontalSpacer_50 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_50)

        self.camerafilebtn = QPushButton(self.widget_11)
        self.camerafilebtn.setObjectName(u"camerafilebtn")
        self.camerafilebtn.setIcon(icon8)
        self.camerafilebtn.setIconSize(QSize(25, 25))

        self.horizontalLayout_28.addWidget(self.camerafilebtn)


        self.horizontalLayout_10.addWidget(self.widget_11)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer)

        self.widget_13 = QWidget(self.frame_12)
        self.widget_13.setObjectName(u"widget_13")
        sizePolicy8.setHeightForWidth(self.widget_13.sizePolicy().hasHeightForWidth())
        self.widget_13.setSizePolicy(sizePolicy8)
        self.widget_13.setMinimumSize(QSize(0, 30))
        self.widget_13.setBaseSize(QSize(0, 70))
        self.horizontalLayout_12 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.onCambtn = QPushButton(self.widget_13)
        self.onCambtn.setObjectName(u"onCambtn")
        self.onCambtn.setFont(font9)
        self.onCambtn.setLayoutDirection(Qt.LeftToRight)
        self.onCambtn.setAutoFillBackground(False)
        self.onCambtn.setIcon(icon5)
        self.onCambtn.setIconSize(QSize(25, 25))

        self.horizontalLayout_12.addWidget(self.onCambtn)

        self.offCambtn = QPushButton(self.widget_13)
        self.offCambtn.setObjectName(u"offCambtn")
        self.offCambtn.setFont(font9)
        self.offCambtn.setAutoFillBackground(False)
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/camera-off.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.offCambtn.setIcon(icon11)
        self.offCambtn.setIconSize(QSize(25, 25))

        self.horizontalLayout_12.addWidget(self.offCambtn)


        self.horizontalLayout_10.addWidget(self.widget_13)


        self.gridLayout.addWidget(self.frame_12, 1, 0, 1, 2)

        self.mainPages.addWidget(self.cameraPage)

        self.verticalLayout_7.addWidget(self.mainPages)


        self.verticalLayout_5.addWidget(self.mainBodyContent)

        self.popupNotificationContainer = QCustomSlideMenu(self.mainBodyContainer)
        self.popupNotificationContainer.setObjectName(u"popupNotificationContainer")
        self.verticalLayout_13 = QVBoxLayout(self.popupNotificationContainer)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.popupNotificationSubContainer = QWidget(self.popupNotificationContainer)
        self.popupNotificationSubContainer.setObjectName(u"popupNotificationSubContainer")
        self.verticalLayout_14 = QVBoxLayout(self.popupNotificationSubContainer)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_9 = QLabel(self.popupNotificationSubContainer)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font9)

        self.verticalLayout_14.addWidget(self.label_9)

        self.frame_5 = QFrame(self.popupNotificationSubContainer)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_8 = QLabel(self.frame_5)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        font12 = QFont()
        font12.setPointSize(10)
        self.label_8.setFont(font12)

        self.horizontalLayout_7.addWidget(self.label_8, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_14.addWidget(self.frame_5)


        self.verticalLayout_13.addWidget(self.popupNotificationSubContainer)


        self.verticalLayout_5.addWidget(self.popupNotificationContainer)

        self.footerContainer = QWidget(self.mainBodyContainer)
        self.footerContainer.setObjectName(u"footerContainer")
        self.horizontalLayout_8 = QHBoxLayout(self.footerContainer)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.footerContainer)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy2.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy2)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 9, -1, -1)
        self.notificationBtn = QPushButton(self.frame_7)
        self.notificationBtn.setObjectName(u"notificationBtn")
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/bell.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.notificationBtn.setIcon(icon12)
        self.notificationBtn.setIconSize(QSize(16, 16))

        self.horizontalLayout_9.addWidget(self.notificationBtn, 0, Qt.AlignLeft)

        self.label_10 = QLabel(self.frame_7)
        self.label_10.setObjectName(u"label_10")
        font13 = QFont()
        font13.setPointSize(8)
        font13.setBold(True)
        self.label_10.setFont(font13)
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label_10, 0, Qt.AlignRight)


        self.horizontalLayout_8.addWidget(self.frame_7)

        self.sizeGrip = QFrame(self.footerContainer)
        self.sizeGrip.setObjectName(u"sizeGrip")
        self.sizeGrip.setMinimumSize(QSize(30, 30))
        self.sizeGrip.setMaximumSize(QSize(30, 30))
        self.sizeGrip.setFrameShape(QFrame.StyledPanel)
        self.sizeGrip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.sizeGrip)


        self.verticalLayout_5.addWidget(self.footerContainer)

        self.footerContainer.raise_()
        self.popupNotificationContainer.raise_()
        self.mainBodyContent.raise_()
        self.headerContainer.raise_()

        self.horizontalLayout.addWidget(self.mainBodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.mainPages.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Detras", None))
#if QT_CONFIG(tooltip)
        self.menuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.homebtn.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.homebtn.setText(QCoreApplication.translate("MainWindow", u"  Home", None))
#if QT_CONFIG(tooltip)
        self.obdbtn.setToolTip(QCoreApplication.translate("MainWindow", u"OBD Data", None))
#endif // QT_CONFIG(tooltip)
        self.obdbtn.setText(QCoreApplication.translate("MainWindow", u"  Diagnosis", None))
#if QT_CONFIG(tooltip)
        self.imusbtn.setToolTip(QCoreApplication.translate("MainWindow", u"IMU Data", None))
#endif // QT_CONFIG(tooltip)
        self.imusbtn.setText(QCoreApplication.translate("MainWindow", u"  IMU", None))
#if QT_CONFIG(tooltip)
        self.gpsbtn.setToolTip(QCoreApplication.translate("MainWindow", u"GPS Data Coordinate", None))
#endif // QT_CONFIG(tooltip)
        self.gpsbtn.setText(QCoreApplication.translate("MainWindow", u"  GPS Data", None))
#if QT_CONFIG(tooltip)
        self.cambtn.setToolTip(QCoreApplication.translate("MainWindow", u"FER (Facial Expression Recognition)", None))
#endif // QT_CONFIG(tooltip)
        self.cambtn.setText(QCoreApplication.translate("MainWindow", u"  FER", None))
#if QT_CONFIG(tooltip)
        self.helpbtn.setToolTip(QCoreApplication.translate("MainWindow", u"Get more help", None))
#endif // QT_CONFIG(tooltip)
        self.helpbtn.setText(QCoreApplication.translate("MainWindow", u"  Help", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:13pt;\">DETRAS</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"WELCOME SCREEEN", None))
        self.Judul_3.setText(QCoreApplication.translate("MainWindow", u"OBD Data", None))
        self.LoadFileOBD.setText(QCoreApplication.translate("MainWindow", u"Browse File", None))
        self.loadobd1btn1.setText(QCoreApplication.translate("MainWindow", u"OBD 1", None))
        self.loadobd1btn2.setText(QCoreApplication.translate("MainWindow", u"OBD 2", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Please browse OBD File", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"File", None))
        self.showDataOBDcsv.setText("")
        self.obdfilebtn.setText("")
        self.Judul.setText(QCoreApplication.translate("MainWindow", u"OBD Data", None))
        self.LoadFileOBD1.setText(QCoreApplication.translate("MainWindow", u"Browse File", None))
        self.obd1btn1.setText(QCoreApplication.translate("MainWindow", u"OBD 1", None))
        self.obd1btn2.setText(QCoreApplication.translate("MainWindow", u"OBD 2", None))
        ___qtablewidgetitem = self.obdData1.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"RPM", None));
        ___qtablewidgetitem1 = self.obdData1.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Coolant", None));
        ___qtablewidgetitem2 = self.obdData1.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Oil Temp", None));
        self.Judul_2.setText(QCoreApplication.translate("MainWindow", u"OBD Data", None))
        self.LoadFileOBD2.setText(QCoreApplication.translate("MainWindow", u"Browse File", None))
        self.obd2btn1.setText(QCoreApplication.translate("MainWindow", u"OBD 1", None))
        self.obd2btn2.setText(QCoreApplication.translate("MainWindow", u"OBD 2", None))
        ___qtablewidgetitem3 = self.obdData2.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Speed", None));
        ___qtablewidgetitem4 = self.obdData2.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Throttle", None));
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Load Files", None))
        self.BLoadFileInertial.setText(QCoreApplication.translate("MainWindow", u"Browse Files", None))
        self.BImpact.setText(QCoreApplication.translate("MainWindow", u"Impact", None))
        self.BRawDatabtn.setText(QCoreApplication.translate("MainWindow", u"Raw Data Inertial", None))
        self.BQuaternionbtn.setText(QCoreApplication.translate("MainWindow", u"Quaternion", None))
        self.BEulerbtn.setText(QCoreApplication.translate("MainWindow", u"Euler Angle", None))
        self.BSimulationbtn.setText(QCoreApplication.translate("MainWindow", u"Simulation", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Please browse Inertial  File", None))
        self.rawinerfilebtn.setText("")
        self.quaternionfilebtn.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Euler Angle", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Impact File", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Quaternion", None))
        self.eulerfilebtn.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Raw Data IMU", None))
        self.rawinerupBtn.setText("")
        self.eulerupBtn.setText("")
        self.quaternionupBtn.setText("")
        self.impactupBtn.setText("")
        self.impactfilebtn.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Impact Calculation", None))
        self.FLoadFileInertial.setText(QCoreApplication.translate("MainWindow", u"Browse Files", None))
        self.FImpact.setText(QCoreApplication.translate("MainWindow", u"Impact", None))
        self.FRawDatabtn.setText(QCoreApplication.translate("MainWindow", u"Raw Data Inertial", None))
        self.FQuaternionbtn.setText(QCoreApplication.translate("MainWindow", u"Quaternion", None))
        self.FEulerbtn.setText(QCoreApplication.translate("MainWindow", u"Euler Angle", None))
        self.FSimulationbtn.setText(QCoreApplication.translate("MainWindow", u"Simulation", None))
        ___qtablewidgetitem5 = self.ImpactTable.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"timestamp", None));
        ___qtablewidgetitem6 = self.ImpactTable.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Total Acceleration", None));
        ___qtablewidgetitem7 = self.ImpactTable.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Impact Force", None));
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Inertial Measurement Unit", None))
        self.iLoadFileInertial.setText(QCoreApplication.translate("MainWindow", u"Browse Files", None))
        self.iImpact.setText(QCoreApplication.translate("MainWindow", u"Impact", None))
        self.iRawDatabtn.setText(QCoreApplication.translate("MainWindow", u"Raw Data Inertial", None))
        self.iQuaternionbtn.setText(QCoreApplication.translate("MainWindow", u"Quaternion", None))
        self.iEulerbtn.setText(QCoreApplication.translate("MainWindow", u"Euler Angle", None))
        self.iSimulationbtn.setText(QCoreApplication.translate("MainWindow", u"Simulation", None))
        ___qtablewidgetitem8 = self.inertialTable.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"acc_x", None));
        ___qtablewidgetitem9 = self.inertialTable.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"acc_y", None));
        ___qtablewidgetitem10 = self.inertialTable.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"acc_z", None));
        ___qtablewidgetitem11 = self.inertialTable.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"gyro_x", None));
        ___qtablewidgetitem12 = self.inertialTable.horizontalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"gyro_y", None));
        ___qtablewidgetitem13 = self.inertialTable.horizontalHeaderItem(5)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"gyro_z", None));
        ___qtablewidgetitem14 = self.inertialTable.horizontalHeaderItem(6)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"mag_x", None));
        ___qtablewidgetitem15 = self.inertialTable.horizontalHeaderItem(7)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"mag_y", None));
        ___qtablewidgetitem16 = self.inertialTable.horizontalHeaderItem(8)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"mag_z", None));
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Quaternion (Trajectory)    ", None))
        self.qLoadFileInertial.setText(QCoreApplication.translate("MainWindow", u"Browse Files", None))
        self.qImpact.setText(QCoreApplication.translate("MainWindow", u"Impact", None))
        self.qRawDatabtn.setText(QCoreApplication.translate("MainWindow", u"Raw Data Inertial", None))
        self.qQuaternionbtn.setText(QCoreApplication.translate("MainWindow", u"Quaternion", None))
        self.qEulerbtn.setText(QCoreApplication.translate("MainWindow", u"Euler Angle", None))
        self.qSimulationbtn.setText(QCoreApplication.translate("MainWindow", u"Simulation", None))
        ___qtablewidgetitem17 = self.quaternionTable.horizontalHeaderItem(0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"q_w", None));
        ___qtablewidgetitem18 = self.quaternionTable.horizontalHeaderItem(1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"q_x", None));
        ___qtablewidgetitem19 = self.quaternionTable.horizontalHeaderItem(2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"q_y", None));
        ___qtablewidgetitem20 = self.quaternionTable.horizontalHeaderItem(3)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"q_z", None));
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Euler Angle (Orientaion)   ", None))
        self.eLoadFileInertial.setText(QCoreApplication.translate("MainWindow", u"Browse Files", None))
        self.eImpact.setText(QCoreApplication.translate("MainWindow", u"Impact", None))
        self.eRawDatabtn.setText(QCoreApplication.translate("MainWindow", u"Raw Data Inertial", None))
        self.eQuaternionbtn.setText(QCoreApplication.translate("MainWindow", u"Quaternion", None))
        self.eEulerbtn.setText(QCoreApplication.translate("MainWindow", u"Euler Angle", None))
        self.eSimulationbtn.setText(QCoreApplication.translate("MainWindow", u"Simulation", None))
        ___qtablewidgetitem21 = self.eulerTable.horizontalHeaderItem(0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Pitch", None));
        ___qtablewidgetitem22 = self.eulerTable.horizontalHeaderItem(1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Roll", None));
        ___qtablewidgetitem23 = self.eulerTable.horizontalHeaderItem(2)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Yaw", None));
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Simulation                         ", None))
        self.sLoadFileInertial.setText(QCoreApplication.translate("MainWindow", u"Browse Files", None))
        self.sImpact.setText(QCoreApplication.translate("MainWindow", u"Impact", None))
        self.sRawDatabtn.setText(QCoreApplication.translate("MainWindow", u"Raw Data Inertial", None))
        self.sQuaternionbtn.setText(QCoreApplication.translate("MainWindow", u"Quaternion", None))
        self.sEulerbtn.setText(QCoreApplication.translate("MainWindow", u"Euler Angle", None))
        self.sSimulationbtn.setText(QCoreApplication.translate("MainWindow", u"Simulation", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Trajectory", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Free Orientation", None))
        self.simulationPlay.setText("")
        self.simulationStop.setText("")
        ___qtablewidgetitem24 = self.gpsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Longitude", None));
        ___qtablewidgetitem25 = self.gpsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Latitude", None));
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"File", None))
        self.gpsupBtn.setText("")
        self.gpsfilebtn.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"File", None))
        self.camerafilebtn.setText("")
        self.onCambtn.setText(QCoreApplication.translate("MainWindow", u" ON", None))
        self.offCambtn.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Notification", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Notification Message", None))
#if QT_CONFIG(tooltip)
        self.notificationBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Notification", None))
#endif // QT_CONFIG(tooltip)
        self.notificationBtn.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Copyright Detras 2024", None))
    # retranslateUi

