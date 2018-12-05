import sys
import os

from PyQt5.QtGui import QFontDatabase
from PyQt5 import QtCore

from Mask_RCNN import demo
from Yolotest import Detector
from yolo.yolo_net import YOLONet
from utils.timer import Timer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog
import argparse
from Ui.Libraries.Widgets.subPage import Ui_MainWindow
from Faster_RCNN import test
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
        print(self.fileName())
    def oncedectect(self):
        if self.file !='':
            _translate = QtCore.QCoreApplication.translate
            classesall = ['person','car','cat','dog']
            classesallnum=[7,8,15,12]
            detect_timer = Timer()

            yolo = YOLONet(False)
            detector = Detector(yolo)
            detect_timer.tic()
            yolostringresults=detector.image_detector(self.file,classesall)
            yolotime = detect_timer.toc()
            self.yoloTime.setText(_translate("MainWindow", str(yolotime)+'s'))
            pixmap = QPixmap("D:\\result.jpg")
            self.yolo_result.setPixmap(pixmap)
            self.yolo_result.setScaledContents(True)

            self.maskRCNN = demo.MaskRCNN()
            detect_timer.tic()
            maskRCNNstringresults=self.maskRCNN.detect(self.file,classesall)
            MaskRCNNtime = detect_timer.toc()
            self.maskTime.setText(_translate("MainWindow", str(MaskRCNNtime)+'s'))
            pixmap = QPixmap("D:\\result2.jpg")
            self.Mask_result.setPixmap(pixmap)
            self.Mask_result.setScaledContents(True)

            detect_timer.tic()
            ssdstringresult=ssd_notebook.dome(self.file,classesallnum)
            SSDtime = detect_timer.toc()
            self.ssdTime.setText(_translate("MainWindow", str(SSDtime)+'s'))
            pixmap = QPixmap("D:\\result3.jpg")
            self.SSD_result.setPixmap(pixmap)
            self.SSD_result.setScaledContents(True)

            detect_timer.tic()
            fasterrcnnresult=test.dectect(self.file,classesall)
            fasterTime=detect_timer.toc()
            self.fasterTime.setText(_translate("MainWindow", str(fasterTime) + 's'))
            pixmap = QPixmap(r"D:\result4.jpg")
            self.Faster_result.setPixmap(pixmap)
            self.Faster_result.setScaledContents(True)
    def fileName(self):
        if self.file!='':
            return self.file.split('/')[len(self.file.split('/'))-1]