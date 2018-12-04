# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'charts.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtCore import pyqtSignal
import pymysql
import os
from PyQt5.QtGui import QPixmap
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456', db='mysql', charset='utf8', )

        self.cur = self.conn.cursor()

        self.sqlstring = "select * from datalist "
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1374, 854)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.chart = QtWidgets.QLabel(self.centralwidget)
        self.chart.setGeometry(QtCore.QRect(30, 110, 661, 651))
        self.chart.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.chart.setObjectName("chart")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 60, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(730, 50, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(570, 70, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.find = QtWidgets.QPushButton(self.centralwidget)
        self.find.setGeometry(QtCore.QRect(960, 170, 75, 23))
        self.find.setObjectName("find")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(760, 122, 61, 20))
        self.label.setObjectName("label")
        self.pic = QtWidgets.QLineEdit(self.centralwidget)
        self.pic.setGeometry(QtCore.QRect(840, 120, 113, 20))
        self.pic.setObjectName("pic")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1000, 120, 54, 16))
        self.label_3.setObjectName("label_3")
        self.al = QtWidgets.QLineEdit(self.centralwidget)
        self.al.setGeometry(QtCore.QRect(1090, 120, 113, 20))
        self.al.setObjectName("al")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(810, 230, 401, 531))
        self.tableWidget.setMaximumSize(QtCore.QSize(401, 16777215))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1374, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.find.clicked.connect(self.find_btn)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.slot)

    def find_btn(self):
        self.pyqt_clicked2.emit()
    def slot(self):
        self.pyqt_clicked1.emit()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.chart.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "算法对比图"))
        self.label_4.setText(_translate("MainWindow", "详细输出"))
        self.pushButton.setText(_translate("MainWindow", "刷新"))
        self.find.setText(_translate("MainWindow", "查询"))
        self.label.setText(_translate("MainWindow", "图片名称"))
        self.label_3.setText(_translate("MainWindow", "  算法"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "图片名称"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "算法"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "识别结果"))
    def slot_button(self):
        os.system("view.py")
        pix = QPixmap('algorithmtime.png')
        self.chart.setPixmap(pix)


    def find_button(self):
        is_first = True
        print(1)
        temp_sqlstring = self.sqlstring
        if self.pic.text() != -1:
            is_first = False
            temp_sqlstring += "where pictureName='" + self.pic.text() + "'"

            if self.al.text() != -1:
                if is_first == True:
                    temp_sqlstring += "where algorithm='" + self.al.text() + "'"
                else:
                    is_first = False
                    temp_sqlstring += "and algorithm='" + self.al.text() + "'"
        self.result_out.clearContents()  # 每一次查询时清除表格中信息

        print(temp_sqlstring)
        self.cur.execute(temp_sqlstring)
        rows = self.cur.fetchall()

        for i in rows:
            print("----------", i)
            for j in 4:
                newItem = QtWidgets.QTableWidgetItem(i[j])
                self.tableWidget.setItem(i,j, newItem)

class MyWindow(QMainWindow,Ui_MainWindow):
    pyqt_clicked1 = pyqtSignal()
    pyqt_clicked2 = pyqtSignal()


    def __init__(self):
        super(MyWindow,self).__init__()
        self.setupUi(self)
        self.pyqt_clicked1.connect(self.slot_button)
        self.pyqt_clicked2.connect(self.find_button)


if __name__=="__main__":
    app=QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    my=MyWindow()
    my.show()
    sys.exit(app.exec_())









