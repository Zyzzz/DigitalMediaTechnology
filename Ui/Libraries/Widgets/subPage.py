# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subPage.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog


#
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1374, 854)
        MainWindow.setStyleSheet("")
        MainWindow.setStyleSheet("\n"
                                 "background-color: rgb(208, 233, 198);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color:#d0e9c6;")
        self.origin = QtWidgets.QLabel(self.centralwidget)
        self.origin.setGeometry(QtCore.QRect(5, 250, 360, 301))
        self.origin.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.origin.setObjectName("origin")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 560, 220, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(220, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(120, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.yolo_result = QtWidgets.QLabel(self.centralwidget)
        self.yolo_result.setGeometry(QtCore.QRect(370, 30, 490, 345))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yolo_result.sizePolicy().hasHeightForWidth())
        self.yolo_result.setSizePolicy(sizePolicy)
        self.yolo_result.setMaximumSize(QtCore.QSize(500, 500))
        self.yolo_result.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.yolo_result.setText("")
        self.yolo_result.setObjectName("yolo_result")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(380, 10, 50, 16))
        self.label.setObjectName("label")
        self.Mask_result = QtWidgets.QLabel(self.centralwidget)
        self.Mask_result.setGeometry(QtCore.QRect(370, 430, 490, 345))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Mask_result.sizePolicy().hasHeightForWidth())
        self.Mask_result.setSizePolicy(sizePolicy)
        self.Mask_result.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.Mask_result.setText("")
        self.Mask_result.setObjectName("Mask_result")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(380, 410, 87, 16))
        self.label_9.setObjectName("label_9")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(890, 410, 94, 16))
        self.label_13.setObjectName("label_13")
        self.Faster_result = QtWidgets.QLabel(self.centralwidget)
        self.Faster_result.setGeometry(QtCore.QRect(870, 430, 490, 345))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Faster_result.sizePolicy().hasHeightForWidth())
        self.Faster_result.setSizePolicy(sizePolicy)
        self.Faster_result.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.Faster_result.setText("")
        self.Faster_result.setObjectName("Faster_result")
        self.SSD_result = QtWidgets.QLabel(self.centralwidget)
        self.SSD_result.setGeometry(QtCore.QRect(870, 30, 490, 345))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SSD_result.sizePolicy().hasHeightForWidth())
        self.SSD_result.setSizePolicy(sizePolicy)
        self.SSD_result.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.SSD_result.setText("")
        self.SSD_result.setObjectName("SSD_result")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(960, 10, 50, 16))
        self.label_5.setObjectName("label_5")
        self.yoloTime = QtWidgets.QLabel(self.centralwidget)
        self.yoloTime.setGeometry(QtCore.QRect(440, 380, 261, 16))
        self.yoloTime.setObjectName("yoloTime")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(400, 380, 31, 16))
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(900, 380, 33, 16))
        self.label_7.setObjectName("label_7")
        self.ssdTime = QtWidgets.QLabel(self.centralwidget)
        self.ssdTime.setGeometry(QtCore.QRect(940, 380, 241, 16))
        self.ssdTime.setObjectName("ssdTime")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(400, 780, 33, 16))
        self.label_11.setObjectName("label_11")
        self.maskTime = QtWidgets.QLabel(self.centralwidget)
        self.maskTime.setGeometry(QtCore.QRect(440, 780, 251, 16))
        self.maskTime.setObjectName("maskTime")
        self.fasterTime = QtWidgets.QLabel(self.centralwidget)
        self.fasterTime.setGeometry(QtCore.QRect(950, 780, 261, 16))
        self.fasterTime.setObjectName("fasterTime")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(910, 780, 33, 16))
        self.label_15.setObjectName("label_15")
        self.origin.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1374, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionopen_files = QtWidgets.QAction(MainWindow)
        self.actionopen_files.setObjectName("actionopen_files")
        self.menuFile.addAction(self.actionopen_files)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.origin.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton.setText(_translate("MainWindow", "开始检测"))
        self.label.setText(_translate("MainWindow", "Yolo算法"))
        self.label_9.setText(_translate("MainWindow", "MaskRCNN算法"))
        self.label_13.setText(_translate("MainWindow", "FasterRCNN算法"))
        self.label_5.setText(_translate("MainWindow", "SSD算法"))
        self.yoloTime.setText(_translate("MainWindow", "TextLabel"))
        self.label_4.setText(_translate("MainWindow", "时间："))
        self.label_7.setText(_translate("MainWindow", "时间："))
        self.ssdTime.setText(_translate("MainWindow", "TextLabel"))
        self.label_11.setText(_translate("MainWindow", "时间："))
        self.maskTime.setText(_translate("MainWindow", "TextLabel"))
        self.fasterTime.setText(_translate("MainWindow", "TextLabel"))
        self.label_15.setText(_translate("MainWindow", "时间："))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionopen_files.setText(_translate("MainWindow", "open files"))

