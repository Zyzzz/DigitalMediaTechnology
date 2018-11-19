#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2018年2月6日
@author: Irony."[讽刺]
@site: http://alyl.vip, http://orzorz.vip, https://coding.net/u/892768447, https://github.com/892768447
@email: 892768447@qq.com
@file: Libraries.Widgets.SearchWidget
@description: 
'''
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QLineEdit, QWidget, QHBoxLayout,QLabel,QListWidget,QListWidgetItem
from PyQt5.QtGui import QIcon
from random import randint

from Libraries.Widgets.RubberBandButton import RubberBandButton


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2018 Irony.\"[讽刺]"
__Version__ = "Version 1.0"


class SearchWidget(QWidget):

    def __init__(self, *args, **kwargs):
        super(SearchWidget, self).__init__(*args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self._initView()

    def _initView(self):
        '''初始化布局'''
        layout = QHBoxLayout(self, spacing=0)
        layout.setContentsMargins(0, 0, 0, 0)
        # 左侧列表
        self.listWidget = QListWidget(self)
        layout.addWidget(self.listWidget)
        # 去掉边框
        self.listWidget.setFrameShape(QListWidget.NoFrame)
        # 隐藏滚动条
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # 这里就用一般的文本配合图标模式了(也可以直接用Icon模式,setViewMode)
        item1 = QListWidgetItem()
        # 设置item的默认宽高(这里只有高度比较有用)
        item1.setSizeHint(QSize(16777215, 30))
        # 文字居中
        item1.setTextAlignment(Qt.AlignLeft)
        item1.setText("数媒课程设计")
        self.listWidget.addItem(item1)

        item2 = QListWidgetItem()
        # 设置item的默认宽高(这里只有高度比较有用)
        item2.setSizeHint(QSize(16777215, 30))
        # 文字居中
        item2.setTextAlignment(Qt.AlignLeft)
        item2.setText("题目：对象检测")
        self.listWidget.addItem(item2)

        item3 = QListWidgetItem()
        # 设置item的默认宽高(这里只有高度比较有用)
        item3.setSizeHint(QSize(16777215, 30))
        # 文字居中
        item3.setTextAlignment(Qt.AlignLeft)
        item3.setText("")
        self.listWidget.addItem(item3)

        item4 = QListWidgetItem()
        # 设置item的默认宽高(这里只有高度比较有用)
        item4.setSizeHint(QSize(16777215, 30))
        # 文字居中
        item4.setTextAlignment(Qt.AlignLeft)
        item4.setText("")
        self.listWidget.addItem(item4)

        item5 = QListWidgetItem()
        # 设置item的默认宽高(这里只有高度比较有用)
        item5.setSizeHint(QSize(16777215, 30))
        # 文字居中
        item5.setTextAlignment(Qt.AlignLeft)
        item5.setText("小组成员：")
        self.listWidget.addItem(item5)

        item6 = QListWidgetItem()
        # 设置item的默认宽高(这里只有高度比较有用)
        item6.setSizeHint(QSize(16777215, 30))
        # 文字居中
        item6.setTextAlignment(Qt.AlignCenter)
        item6.setText("刘青")
        self.listWidget.addItem(item6)

        item7 = QListWidgetItem()
        # 设置item的默认宽高(这里只有高度比较有用)
        item7.setSizeHint(QSize(16777215, 30))
        # 文字居中
        item7.setTextAlignment(Qt.AlignCenter)
        item7.setText("周炎")
        self.listWidget.addItem(item7)

        item8 = QListWidgetItem()
        # 设置item的默认宽高(这里只有高度比较有用)
        item8.setSizeHint(QSize(16777215, 30))
        # 文字居中
        item8.setTextAlignment(Qt.AlignCenter)
        item8.setText("熊玲")
        self.listWidget.addItem(item8)

        item9 = QListWidgetItem()
        # 设置item的默认宽高(这里只有高度比较有用)
        item9.setSizeHint(QSize(16777215, 30))
        # 文字居中
        item9.setTextAlignment(Qt.AlignCenter)
        item9.setText("刘湛琦")
        self.listWidget.addItem(item9)

        item10 = QListWidgetItem()
        # 设置item的默认宽高(这里只有高度比较有用)
        item10.setSizeHint(QSize(16777215, 30))
        # 文字居中
        item10.setTextAlignment(Qt.AlignCenter)
        item10.setText("胡吉双")
        self.listWidget.addItem(item10)

        # self._label1 = QLabel(self)
        # self._label1.setText("fdafdfda")
        # self._label2 = QLabel(self)
        # self._label2.setText("fdafdfda")
        # self._label3 = QLabel(self)
        # self._label3.setText("fdafdfda")
        # self._label4 = QLabel(self)
        # self._label4.setText("fdafdfda")
        # layout.addWidget(self._label1)
        # layout.addWidget(self._label2)
        # layout.addWidget(self._label3)
        # layout.addWidget(self._label4)


if __name__ == "__main__":
    import sys
    import os
    os.chdir("../../")
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtGui import QFontDatabase
    app = QApplication(sys.argv)
    QFontDatabase.addApplicationFont("themes/default/font.ttf")
    app.setStyleSheet(open("themes/default/style.qss",
                           "rb").read().decode("utf-8"))
    w = SearchWidget()
    w.show()
    sys.exit(app.exec_())
