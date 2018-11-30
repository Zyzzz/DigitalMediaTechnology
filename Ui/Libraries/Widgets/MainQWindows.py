import sys
import os

from PyQt5.QtGui import QFontDatabase

from Mask_RCNN import demo
from Yolotest import Detector
from yolo.yolo_net import YOLONet
from utils.timer import Timer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog
import argparse
from Ui.Libraries.Widgets.MainWindowUi import Ui_MainWindow
from Faster_RCNN import test
from PyQt5.QtWidgets import QMainWindow, QApplication,QGraphicsScene
from SSD import ssd_notebook
class MainWindows(QMainWindow,Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        super().__init__()
        self.initUI()
        self.file=''
        self.classes = []
    def initUI(self):
        self.setupUi(self)
        self.actionOpen_File.triggered.connect(self.openMsg)
        self.pushButton.clicked.connect(self.oncle)
        self.show()  # 显示

    def openMsg(self):
        self.file, ok = QFileDialog.getOpenFileName(self, "打开","F:\\", "Images (*.*)")
        self.pixmap=QPixmap(self.file)
        self.image1.setPixmap(self.pixmap)
        self.statusbar.showMessage(self.file)
        self.image1.setScaledContents (True)

    def oncle(self):
        if self.file !='':
            if self.checkBox.isChecked():
                self.classes.append("person")
            if self.checkBox_2.isChecked():
                self.classes.append("car")
            if self.checkBox_3.isChecked():
                self.classes.append("cat")
            if self.checkBox_4.isChecked():
                self.classes.append("dog")
            if self.comboBox.currentText() =="YOLO":
                yolo = YOLONet(False)
                detector = Detector(yolo)
                # detect from camera
                # cap = cv2.VideoCapture(-1)
                # detector.camera_detector(cap)
                # detect from image file
                imname = self.file
                detector.image_detector(imname,self.classes)
                pixmap = QPixmap("D:\\result.jpg")
                self.image2.setPixmap(pixmap)
                self.image2.setScaledContents(True)
            elif self.comboBox.currentText() =="MaskRCNN":
                self.maskRCNN = demo.MaskRCNN()
                self.maskRCNN.detect(self.file,self.classes)
                scene = QGraphicsScene()
                pixmap = QPixmap("D:\\result2.jpg")
                self.image2.setPixmap(pixmap)
                self.image2.setScaledContents(True)
            elif self.comboBox.currentText() =="SSD":
                classes1=[]
                for item in self.classes:
                    if(item=='person'):
                        classes1.append(15)
                    elif(item=='dog'):
                        classes1.append(12)
                    elif(item=='cat'):
                        classes1.append(8)
                    elif(item=='car'):
                        classes1.append(7)
                ssd_notebook.dome(self.file,classes1)
                pixmap = QPixmap("D:\\result3.jpg")
                self.image2.setPixmap(pixmap)
                self.image2.setScaledContents(True)
            elif self.comboBox.currentText() =="FasterRCNN":
                test.dectect(self.file,self.classes)
                pixmap = QPixmap("D:\\result4.png")
                self.image2.setPixmap(pixmap)
                self.image2.setScaledContents(True)
        self.classes.clear()
