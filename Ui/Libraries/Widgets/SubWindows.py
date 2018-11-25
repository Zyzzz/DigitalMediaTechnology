import sys
import os

from PyQt5.QtGui import QFontDatabase
from qtpy import QtCore

from Mask_RCNN import demo
from Yolotest import Detector
from yolo.yolo_net import YOLONet
from utils.timer import Timer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog
import argparse
from Ui.Libraries.Widgets.subPage import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication,QGraphicsScene
from SSD import ssd_notebook
class SubWindows(QMainWindow,Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        super().__init__()
        self.file=''
        self.initUI()
        self.classes = []
    def initUI(self):
        self.setupUi(self)
        self.actionopen_files.triggered.connect(self.openMsg)
        self.pushButton.clicked.connect(self.oncedectect)
        self.show()  # 显示
    def openMsg(self):
        self.file, ok = QFileDialog.getOpenFileName(self, "打开","D:\\", "Images (*.*)")
        self.pixmap=QPixmap(self.file)
        self.origin.setPixmap(self.pixmap)
        self.statusbar.showMessage(self.file)
        self.origin.setScaledContents (True)
    def oncedectect(self):
        if self.file !='':
            _translate = QtCore.QCoreApplication.translate
            classesall = ['person','car','cat','dog']
            classesallnum=[7,8,15,12]
            detect_timer = Timer()

            yolo = YOLONet(False)
            detector = Detector(yolo)
            imname = self.file
            detect_timer.tic()
            detector.image_detector(imname,classesall)
            self.yoloTime.setText(_translate("MainWindow", str(detect_timer.toc())+'s'))
            pixmap = QPixmap("D:\\result.jpg")
            self.yolo_result.setPixmap(pixmap)
            self.yolo_result.setScaledContents(True)

            self.maskRCNN = demo.MaskRCNN()
            detect_timer.tic()
            self.maskRCNN.detect(self.file,classesall)
            self.maskTime.setText(_translate("MainWindow", str(detect_timer.toc())+'s'))
            pixmap = QPixmap("D:\\result2.jpg")
            self.Mask_result.setPixmap(pixmap)
            self.Mask_result.setScaledContents(True)

            detect_timer.tic()
            ssd_notebook.dome(self.file,classesallnum)
            self.ssdTime.setText(_translate("MainWindow", str(detect_timer.toc())+'s'))
            pixmap = QPixmap("D:\\result3.jpg")
            self.SSD_result.setPixmap(pixmap)
            self.SSD_result.setScaledContents(True)

            # test.dectect(self.file,self.classes)
            # pixmap = QPixmap("D:\\result4.png")
            # self.image2.setPixmap(pixmap)
            # self.image2.setScaledContents(True)