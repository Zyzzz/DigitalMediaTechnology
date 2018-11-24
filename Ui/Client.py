#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2018年2月6日
@author: Irony."[讽刺]
@site: http://alyl.vip, http://orzorz.vip, https://coding.net/u/892768447, https://github.com/892768447
@email: 892768447@qq.com
@file: Client
@description: 
'''
import sys
import Ui.config

from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWidgets import QApplication

from Ui.Libraries.Widgets.MainWidget import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    QFontDatabase.addApplicationFont("themes/default/font.ttf")
    app.setStyleSheet(open("themes/default/style.qss",
                           "rb").read().decode("utf-8"))
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
