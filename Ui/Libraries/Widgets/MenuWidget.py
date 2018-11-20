#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2018年2月6日
@author: Irony."[讽刺]
@site: http://alyl.vip, http://orzorz.vip, https://coding.net/u/892768447, https://github.com/892768447
@email: 892768447@qq.com
@file: Libraries.Widgets.MenuWidget
@description: 
'''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QSpacerItem, QSizePolicy, QTreeWidget,\
    QVBoxLayout, QHBoxLayout

from Ui.Libraries.Widgets.AvatarWidget import AvatarWidget
from Ui.Libraries.Widgets.SearchWidget import SearchWidget


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2018 Irony.\"[讽刺]"
__Version__ = "Version 1.0"


class MenuWidget(QWidget):

    def __init__(self, *args, **kwargs):
        super(MenuWidget, self).__init__(*args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        # 初始化布局和控件
        self._initView()

    def _initView(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 30, 20, 30)
        layout.setSpacing(20)
        # 头像
        hlayout = QHBoxLayout()
        hlayout.addItem(QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        hlayout.addWidget(AvatarWidget(self))
        hlayout.addItem(QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        layout.addLayout(hlayout, 1)
        # 搜索框
        layout.addWidget(SearchWidget(self), 1)
        # 目录
        self._menuTree = QTreeWidget(self)
        self._menuTree.setFrameShape(QTreeWidget.NoFrame)
        self._menuTree.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self._menuTree.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self._menuTree.setEditTriggers(QTreeWidget.NoEditTriggers)
        self._menuTree.setIndentation(0)  # 去掉缩进
        self._menuTree.setAnimated(True)
        self._menuTree.setHeaderHidden(True)
        layout.addWidget(self._menuTree, 4)
# 美化样式表
Stylesheet = """
/*去掉item虚线边框*/
QListWidget, QListView, QTreeWidget, QTreeView {
    outline: 0px;
}
/*设置左侧选项的最小最大宽度,文字颜色和背景颜色*/
QListWidget {
    min-width: 120px;
    max-width: 120px;
    color: white;
    background: black;
}
/*被选中时的背景颜色和左边框颜色*/
QListWidget::item:selected {
    background: rgb(52, 52, 52);
    border-left: 2px solid rgb(9, 187, 7);
}
/*鼠标悬停颜色*/
HistoryPanel::item:hover {
    background: rgb(52, 52, 52);
}

/*右侧的层叠窗口的背景颜色*/
QStackedWidget {
    background: rgb(30, 30, 30);
}
/*模拟的页面*/
QLabel {
    color: white;
}
"""

if __name__ == "__main__":
    import sys
    import os
    os.chdir("../../")
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtGui import QFontDatabase
    app = QApplication(sys.argv)
    QFontDatabase.addApplicationFont("themes/default/font.ttf")
    app.setStyleSheet(Stylesheet)
    w = MenuWidget()
    w.resize(800, 600)
    w.show()
    sys.exit(app.exec_())
