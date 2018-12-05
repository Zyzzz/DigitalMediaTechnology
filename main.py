# !/usr/bin/python3
# -*- coding: utf-8 -*-


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
from MainWindowUI import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication,QGraphicsScene
from SSD import ssd_notebook
from Ui.Libraries.Widgets.MainWidget import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    QFontDatabase.addApplicationFont("Ui/themes/default/font.ttf")
    app.setStyleSheet(open("Ui/themes/default/style.qss",
                           "rb").read().decode("utf-8"))
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())