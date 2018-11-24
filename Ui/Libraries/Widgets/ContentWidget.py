#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2018年2月6日
@author: Irony."[讽刺]
@site: http://alyl.vip, http://orzorz.vip, https://coding.net/u/892768447, https://github.com/892768447
@email: 892768447@qq.com
@file: Libraries.Widgets.ContentWidget
@description: 
'''
from random import randint
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtWidgets import QWidget, QProgressBar, QVBoxLayout,QLabel,QStackedWidget,QMainWindow
from Ui.Libraries.Widgets import MainWindowUi
from Ui.Libraries.Widgets import subPage
import argparse
from SSD import ssd_notebook
from Mask_RCNN import demo
from Yolotest import Detector
from yolo.yolo_net import YOLONet
import threading
# from Faster_RCNN import test
__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2018 Irony.\"[讽刺]"
__Version__ = "Version 1.0"


class ContentWidget(QWidget,MainWindowUi.Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super(ContentWidget, self).__init__(*args, **kwargs)
        # 保证qss有效
        self.setAttribute(Qt.WA_StyledBackground, True)
        self._initView()
        self.classes = []
    def _initView(self):
        '''进度条'''
        layout = QVBoxLayout(self, spacing=0)
        layout.setContentsMargins(0, 0, 0, 0)
        self._progressBar = QProgressBar(self, textVisible=False)
        layout.addWidget(self._progressBar)
        self.stackedWidget = QStackedWidget(self)
        layout.addWidget(self.stackedWidget)
        MainWindow = QMainWindow()
        self.setupUi(MainWindow)
        MainWindow.setStyleSheet(open("themes/default/style.qss",
                                "rb").read().decode("utf-8"))
        self.stackedWidget.addWidget(MainWindow)
        SubWindow = QMainWindow()
        ui = subPage.Ui_MainWindow()
        ui.setupUi(SubWindow)
        SubWindow.setStyleSheet(open("themes/default/style.qss",
                                "rb").read().decode("utf-8"))
        self.stackedWidget.addWidget(SubWindow)

        self.actionOpen_File.triggered.connect(self.openMsg)
        self.pushButton.clicked.connect(self.oncle)
        # for i in range(3):
        #     label = QLabel('我是页面 %d' % i, self)
        #     label.setAlignment(Qt.AlignCenter)
        #     # 设置label的背景颜色(这里随机)
        #     # 这里加了一个margin边距(方便区分QStackedWidget和QLabel的颜色)
        #     label.setStyleSheet('background: rgb(%d, %d, %d);margin: 3px;' %(39,174,97))
        #     self.stackedWidget.addWidget(label)
        #     self.stackedWidget.addWidget(QProgressBar(self, textVisible=True))

    def dochange(self):
        self.stackedWidget.setCurrentIndex(1)
        self.show()
        print('23')

    def openMsg(self):
        self.file, ok = QFileDialog.getOpenFileName(self, "打开","F:\\", "Images (*.*)")
        self.pixmap=QPixmap(self.file)
        self.image1.setPixmap(self.pixmap)
        self.statusbar.showMessage(self.file)
        self.image1.setScaledContents (True)
    def oncle(self):
        if self.statusbar.currentMessage()!='':
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
                scene = QGraphicsScene()
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
                # test.dectect(self.file,self.classes)
                pixmap = QPixmap("D:\\result4.png")
                self.image2.setPixmap(pixmap)
                self.image2.setScaledContents(True)
        self.classes.clear()

if __name__ == "__main__":
    import sys
    import os
    os.chdir("../../")
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    app.setStyleSheet(open("themes/default/style.qss",
                           "rb").read().decode("utf-8"))
    w = ContentWidget()
    w.resize(800, 600)
    w.show()
    sys.exit(app.exec_())
