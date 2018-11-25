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
from PyQt5.QtWidgets import QWidget, QProgressBar, QVBoxLayout,QLabel,QStackedWidget,QMainWindow
from Ui.Libraries.Widgets.SubWindows import SubWindows
from Ui.Libraries.Widgets.MainQWindows import MainWindows
# from Faster_RCNN import test
__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2018 Irony.\"[讽刺]"
__Version__ = "Version 1.0"


class ContentWidget(QWidget):

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
        MainWindow = MainWindows()
        MainWindow.setStyleSheet(open("Ui/themes/default/style.qss",
                                "rb").read().decode("utf-8"))
        self.stackedWidget.addWidget(MainWindow)
        subWindows = SubWindows()
        subWindows.setStyleSheet(open("Ui/themes/default/style.qss",
                                "rb").read().decode("utf-8"))
        self.stackedWidget.addWidget(subWindows)
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
