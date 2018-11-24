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
from Ui.Libraries.Widgets.subPage import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication,QGraphicsScene
from SSD import ssd_notebook

class SubWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        super().__init__()
        self.initUI()
        self.classes = []
        print("self.statusbar.currentMessage():",self.statusbar.currentMessage())
    def initUI(self):
        self.setupUi(self)
        self.actionopen_files.triggered.connect(self.openMsg)
        # self.pushButton.clicked.connect(self.oncle)
        self.show()

