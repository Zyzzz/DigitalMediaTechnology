# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'charts.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QApplication,QTableWidget,QTableWidgetItem
from PyQt5.QtCore import pyqtSignal
import pymysql
import os
from PyQt5.QtGui import QPixmap
import sys
import plotly.plotly as py
import plotly.graph_objs as pg
from plotly.graph_objs import Scatter, Layout


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456', db='mysql', charset='utf8', )

        self.cur = self.conn.cursor()

        self.sqlstring = "select * from datalist "
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1374, 854)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color:#d0e9c6;")
        self.chart = QtWidgets.QLabel(self.centralwidget)
        self.chart.setGeometry(QtCore.QRect(60, 160, 661, 651))
        self.chart.setFixedSize(QtCore.QSize(620, 600))
        self.chart.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.chart.setObjectName("chart")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 80, 151, 51))
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
        self.pushButton.setGeometry(QtCore.QRect(550, 100, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.find = QtWidgets.QPushButton(self.centralwidget)
        self.find.setGeometry(QtCore.QRect(1250, 116, 75, 23))
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
        self.tableWidget.setGeometry(QtCore.QRect(750, 170, 401, 531))
        self.tableWidget.setFixedSize(QtCore.QSize(570, 590))
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
        db = pymysql.connect("localhost", "root", "123456", "mysql")

        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        lists = [[], []]
        lists[0].append('YOLO')
        lists[0].append('SSD')
        lists[0].append('MaskRCNN')
        lists[0].append('FasterRCNN')

        # 使用 execute()  方法执行 SQL 查询
        cursor.execute("select avg(time) from algorithmtime where algorithm='YOLO';")
        rows = cursor.fetchone()
        print(rows)
        lists[1].append(rows[0])
        cursor.execute("select avg(time) from algorithmtime where algorithm='SSD';")
        rows = cursor.fetchone()
        print(rows)
        lists[1].append(rows[0])
        print(lists)
        cursor.execute("select avg(time) from algorithmtime where algorithm='MaskRCNN';")
        rows = cursor.fetchone()
        lists[1].append(rows[0])
        cursor.execute("select avg(time) from algorithmtime where algorithm='FasterRCNN';")
        rows = cursor.fetchone()
        lists[1].append(rows[0])

        # print(lists)

        # print(lists[0])

        # print(([x[0] for x in lists]))

        date_time = pg.Bar(x=lists[0], y=lists[1], name='运行时间')

        data = [date_time]

        # barmode = [stack,group,overlay,relative]

        layout = pg.Layout(barmode='group', title="Average running time of the algorithm")
        fig = pg.Figure(data=data, layout=layout)
        py.sign_in('templarz', 'PtKMjV9gAzINZqmQRU4T')
        py.image.save_as(fig, filename='algorithmtime.png')

        from IPython.display import Image
        Image('algorithmtime.png')

        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchone()

        print("Database version : %s " % data)

        # 关闭数据库连接
        db.close()
        pix = QPixmap('algorithmtime.png')
        self.chart.setPixmap(pix)
        self.chart.setScaledContents(True)


    def find_button(self):
        is_first = True
        print(1)
        temp_sqlstring = self.sqlstring
        pictureName = self.pic.text()
        algorithm = self.al.text()

        if pictureName != -1:
            is_first = False
            temp_sqlstring += "where pictureName='" + pictureName + "'"
            if algorithm != -1:
                if is_first == True:
                    temp_sqlstring += "where algorithm='" + algorithm + "'"
                else:
                    is_first = False
                    temp_sqlstring += "and algorithm='" + algorithm + "'"
        # self.result_out.clearContents()  # 每一次查询时清除表格中信息
        if(temp_sqlstring == "select * from datalist where pictureName=''and algorithm=''"):
            temp_sqlstring = "select * from datalist"
        if(pictureName=='' and algorithm!=''):
            temp_sqlstring = "select * from datalist where algorithm= " +"\'"+algorithm+"\'"
        if(pictureName!='' and algorithm==''):
            temp_sqlstring = "select * from datalist where pictureName= " +"\'"+pictureName+"\'"
        print(temp_sqlstring)
        self.cur.execute(temp_sqlstring.replace('\\', ''))
        rows = self.cur.fetchall()
        row = self.cur.rowcount
        vol = len(rows[0])
        self.tableWidget.setRowCount(row)
        self.tableWidget.setColumnCount(vol)

        for i in range(row):
            for j in range(vol):
                temp_data = rows[i][j]  # 临时记录，不能直接插入表格
                data = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                self.tableWidget.setItem(i, j, data)

        # for i in rows:
        #     print("----------", i)
        #     for j in 4:
        #         newItem = QtWidgets.QTableWidgetItem(i[j])
        #         self.tableWidget.setItem(i,j, newItem)

class ChartsWindow(QMainWindow,Ui_MainWindow):
    pyqt_clicked1 = pyqtSignal()
    pyqt_clicked2 = pyqtSignal()


    def __init__(self):
        super(ChartsWindow,self).__init__()
        self.setupUi(self)
        self.pyqt_clicked1.connect(self.slot_button)
        self.pyqt_clicked2.connect(self.find_button)


if __name__=="__main__":
    app=QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    my=ChartsWindow()
    my.show()
    sys.exit(app.exec_())









