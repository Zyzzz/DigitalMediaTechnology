# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Py40 PyQt5 tutorial

This program creates a statusbar.

author: Jan Bodnar
website: py40.com
last edited: January 2015
"""

import sys
import os

from Mask_RCNN import demo
from Yolotest import Detector
from yolo.yolo_net import YOLONet
from utils.timer import Timer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog
import argparse
from MainWindowUI import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication,QGraphicsScene

class MyApp(QMainWindow,Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setupUi(self)
        self.actionOpen_File.triggered.connect(self.openMsg)
        self.pushButton.clicked.connect(self.oncle)
        self.show()  # 显示
    def openMsg(self):
        self.file, ok = QFileDialog.getOpenFileName(self, "打开","F:\\", "Images (*.*)")
        self.scene=QGraphicsScene()
        self.pixmap=QPixmap(self.file)
        self.scene.addPixmap(self.pixmap)
        self.graphicsView.setScene(self.scene)
        self.statusbar.showMessage(self.file)
    def oncle(self):
        if self.comboBox.currentText() =="YOLO":
            parser = argparse.ArgumentParser()
            parser.add_argument('--weights', default="YOLO_small.ckpt", type=str)
            parser.add_argument('--weight_dir', default='weights', type=str)
            parser.add_argument('--data_dir', default="data", type=str)
            parser.add_argument('--gpu', default='', type=str)
            args = parser.parse_args()
            os.environ['CUDA_VISIBLE_DEVICES'] = args.gpu
            yolo = YOLONet(False)
            weight_file = os.path.join(args.data_dir, args.weight_dir, args.weights)
            detector = Detector(yolo, weight_file)
            # detect from camera
            # cap = cv2.VideoCapture(-1)
            # detector.camera_detector(cap)
            # detect from image file
            imname = self.file
            detector.image_detector(imname)
            scene = QGraphicsScene()
            pixmap = QPixmap("D:\\result.jpg")
            scene.addPixmap(pixmap)
            self.graphicsView_2.setScene(scene)
        elif self.comboBox.currentText() =="MaskRCNN":
            self.maskRCNN = demo.MaskRCNN()
            self.maskRCNN.detect(self.file)
            scene = QGraphicsScene()
            pixmap = QPixmap("D:\\result3.jpg")
            scene.addPixmap(pixmap)
            self.graphicsView_2.setScene(scene)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())