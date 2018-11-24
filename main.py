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
# class MyApp(QMainWindow,Ui_MainWindow):
#     def __init__(self):
#         QMainWindow.__init__(self)
#         super().__init__()
#         self.initUI()
#         self.classes = []
#         print("self.statusbar.currentMessage():",self.statusbar.currentMessage())
#     def initUI(self):
#         self.setupUi(self)
#         self.actionOpen_File.triggered.connect(self.openMsg)
#         self.pushButton.clicked.connect(self.oncle)
#         self.show()  # 显示
#     def openMsg(self):
#         self.file, ok = QFileDialog.getOpenFileName(self, "打开","I:\\", "Images (*.*)")
#         self.scene=QGraphicsScene()
#         self.pixmap=QPixmap(self.file)
#         self.scene.addPixmap(self.pixmap)
#         self.graphicsView.setScene(self.scene)
#         self.statusbar.showMessage(self.file)
#     def oncle(self):
#         if self.statusbar.currentMessage()!='':
#             if self.checkBox.isChecked():
#                 self.classes.append("person")
#             if self.checkBox_2.isChecked():
#                 self.classes.append("car")
#             if self.checkBox_3.isChecked():
#                 self.classes.append("cat")
#             if self.checkBox_4.isChecked():
#                 self.classes.append("dog")
#             if self.comboBox.currentText() =="YOLO":
#                 parser = argparse.ArgumentParser()
#                 parser.add_argument('--weights', default="YOLO_small.ckpt", type=str)
#                 parser.add_argument('--weight_dir', default='weights', type=str)
#                 parser.add_argument('--data_dir', default="data", type=str)
#                 parser.add_argument('--gpu', default='', type=str)
#                 args = parser.parse_args()
#                 os.environ['CUDA_VISIBLE_DEVICES'] = args.gpu
#                 yolo = YOLONet(False)
#                 weight_file = os.path.join(args.data_dir, args.weight_dir, args.weights)
#                 detector = Detector(yolo, weight_file)
#                 # detect from camera
#                 # cap = cv2.VideoCapture(-1)
#                 # detector.camera_detector(cap)
#                 # detect from image file
#                 imname = self.file
#                 detector.image_detector(imname,self.classes)
#                 scene = QGraphicsScene()
#                 pixmap = QPixmap("D:\\result.jpg")
#                 scene.addPixmap(pixmap)
#                 self.graphicsView_2.setScene(scene)
#             elif self.comboBox.currentText() =="MaskRCNN":
#                 self.maskRCNN = demo.MaskRCNN()
#                 self.maskRCNN.detect(self.file,self.classes)
#                 scene = QGraphicsScene()
#                 pixmap = QPixmap("D:\\result3.jpg")
#                 scene.addPixmap(pixmap)
#                 self.graphicsView_2.setScene(scene)
#             elif self.comboBox.currentText() =="SSD":
#                 classes1=[]
#                 for item in self.classes:
#                     if(item=='person'):
#                         classes1.append(15)
#                     elif(item=='dog'):
#                         classes1.append(12)
#                     elif(item=='cat'):
#                         classes1.append(8)
#                     elif(item=='car'):
#                         classes1.append(7)
#                 ssd_notebook.dome(self.file,classes1)
#                 scene = QGraphicsScene()
#                 pixmap = QPixmap("D:\\result2.jpg")
#                 scene.addPixmap(pixmap)
#                 self.graphicsView_2.setScene(scene)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    QFontDatabase.addApplicationFont("Ui/themes/default/font.ttf")
    app.setStyleSheet(open("Ui/themes/default/style.qss",
                           "rb").read().decode("utf-8"))
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())