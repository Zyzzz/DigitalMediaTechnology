#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2018年2月18日
@author: Irony."[讽刺]
@site: http://alyl.vip, http://orzorz.vip, https://coding.net/u/892768447, https://github.com/892768447
@email: 892768447@qq.com
@file: Libraries.Widgets.SkinWidget
@description: 
'''
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGridLayout, QScrollArea, QWidget, QVBoxLayout, QLabel,\
    QSpacerItem, QSizePolicy, QPushButton, QHBoxLayout,\
    QGraphicsDropShadowEffect

from Libraries.Widgets.FramelessWindow import FramelessWindow
from Libraries.Widgets.TitleWidget import TitleWidget


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2018 Irony.\"[讽刺]"
__Version__ = "Version 1.0"


class ThemeItem(QWidget):
    '''网格中的自定义item'''

    clicked = pyqtSignal(str, str, str)

    def __init__(self, file, *args, **kwargs):
        super(ThemeItem, self).__init__(*args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setCursor(Qt.PointingHandCursor)
        self._file = file
        name = os.path.basename(os.path.dirname(file))
        self.setToolTip(name)
        layout = QVBoxLayout(self, spacing=5)
        layout.setContentsMargins(0, 0, 0, 0)
        self.imageLabel = QLabel(self, objectName="imageLabel")
        layout.addWidget(self.imageLabel)
        nameLabel = QLabel(name, self)
        nameLabel.setAlignment(Qt.AlignCenter)
        layout.addWidget(nameLabel)
        self.image_path = os.path.join("themes", name, "preview.png")

    def resizeEvent(self, event):
        # 当控件的大小变动时才设置缩放后的图片
        if os.path.isfile(self.image_path):
            self.imageLabel.setPixmap(
                QPixmap(self.image_path).scaled(self.imageLabel.size()))
        super(ThemeItem, self).resizeEvent(event)

    def mouseReleaseEvent(self, event):
        self.clicked.emit(self.toolTip(), self._file, self.image_path)
        super(ThemeItem, self).mouseReleaseEvent(event)


class GridWidget(QWidget):
    '''网格视图'''

    itemClicked = pyqtSignal(str, str, str)

    def __init__(self, *args, **kwargs):
        super(GridWidget, self).__init__(*args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self._layout = QGridLayout(self, spacing=10)
        self._layout.setContentsMargins(10, 10, 10, 10)

    def init(self, path):
        style_files = []
        for name in os.listdir(path):
            tpath = os.path.join(path, name)
            spath = os.path.join(tpath, "style.qss")
            if not os.path.isdir(tpath) or not os.path.isfile(spath):
                continue
            style_files.append(spath)
        style_files = self.splist(style_files, 5)
        for row, items in enumerate(style_files):
            for col, file in enumerate(items):
                item = ThemeItem(file, self)
                item.clicked.connect(self.itemClicked.emit)
                self._layout.addWidget(item, row, col)
        length = len(style_files)
        if length == 0:
            return
        # 在第一行最后添加伸展条
        self._layout.addItem(QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum), 0, len(style_files[0]))
        # 在第一列最后添加伸展条
        self._layout.addItem(QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding), length, 0)

    def splist(self, src, length):
        # 等分列表
        return [src[i:i + length] for i in range(len(src)) if i % length == 0]


class PreviewImage(QWidget):
    '''主题预览中的图片'''

    def __init__(self, *args, **kwargs):
        super(PreviewImage, self).__init__(*args, **kwargs)
        layout = QHBoxLayout(self)
        self.leftButton = QPushButton(
            self, objectName="leftButton", cursor=Qt.PointingHandCursor, visible=False)
        layout.addWidget(self.leftButton)  # 上一个
        layout.addItem(QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        self.imageLabel = QLabel(self)  # 图片
        # 边缘阴影效果
        effect = QGraphicsDropShadowEffect(self.imageLabel)
        effect.setBlurRadius(40)
        effect.setOffset(0, 0)
        effect.setColor(Qt.gray)
        self.imageLabel.setGraphicsEffect(effect)
        layout.addWidget(self.imageLabel)
        layout.addItem(QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        self.rightButton = QPushButton(
            self, objectName="rightButton", cursor=Qt.PointingHandCursor, visible=False)
        layout.addWidget(self.rightButton)  # 下一个

    def enterEvent(self, event):
        super(PreviewImage, self).enterEvent(event)
        self.leftButton.setVisible(True)
        self.rightButton.setVisible(True)

    def leaveEvent(self, event):
        super(PreviewImage, self).leaveEvent(event)
        self.leftButton.setVisible(False)
        self.rightButton.setVisible(False)

    def setPixmap(self, path, w, h):
        pixmap = QPixmap(path).scaled(w, h)
        self.imageLabel.resize(w, h)
        self.imageLabel.setPixmap(pixmap)


class PreviewWidget(QWidget):
    '''主题预览'''

    choosed = pyqtSignal(str)
    closed = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(PreviewWidget, self).__init__(*args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)  # 支持样式
        layout = QGridLayout(self)
        layout.setVerticalSpacing(20)
        layout.setContentsMargins(10, 10, 10, 30)
        self.previewImage = PreviewImage(self)
        layout.addWidget(self.previewImage, 1, 0, 1, 3)  # 主题预览图片

        layout.addItem(QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum), 2, 0)
        self.titleLabel = QLabel(self, objectName="titleLabel")
        self.titleLabel.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.titleLabel, 2, 1)  # 主题名字
        layout.addItem(QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum), 2, 2)

        layout.addWidget(QPushButton(
            "立即设置", self, clicked=self.onChoosed, objectName="applyButton", cursor=Qt.PointingHandCursor), 3, 1)
        layout.addWidget(QPushButton(
            self, clicked=self.closed.emit, objectName="closeButton", cursor=Qt.PointingHandCursor), 5, 1)  # 关闭按钮

    def init(self, title, path, image):
        self.titleLabel.setText(title)
        self.previewImage.setPixmap(image, int(
            self.width() * 4 / 5), int(self.height() * 2 / 3) - 50)
        self.spath = path

    def onChoosed(self):
        self.choosed.emit(self.spath)


class SkinWidget(FramelessWindow):
    '''主题窗口'''

    TITLE_WIDTH = 36

    def __init__(self, *args, **kwargs):
        super(SkinWidget, self).__init__(*args, **kwargs)
        layout = QVBoxLayout(self, spacing=0)
        layout.setContentsMargins(0, 0, 0, 0)
        self.titleWidget = TitleWidget(
            True, True, False, False, False, False, True, parent=self)
        self.titleWidget.closed.connect(self.close)
        layout.addWidget(self.titleWidget)
        scrollWidget = QScrollArea(self)
        layout.addWidget(scrollWidget)

        scrollWidget.setFrameShape(QScrollArea.NoFrame)
        scrollWidget.setWidgetResizable(True)
        scrollWidget.setAlignment(Qt.AlignCenter)
        scrollWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scrollWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # 网格窗口
        self._widget = GridWidget(scrollWidget)
        scrollWidget.setWidget(self._widget)
        self._widget.itemClicked.connect(self.onItemClicked)
        self._widget.init("themes")
        # 预览
        self.previewWidget = PreviewWidget(self, visible=False)

    def onItemClicked(self, title, path, image):
        if os.path.isfile(image):
            self.resizePreviewWidget()
            self.previewWidget.init(title, path, image)
            self.previewWidget.setVisible(True)

    def resizeEvent(self, event):
        super(SkinWidget, self).resizeEvent(event)
        self.resizePreviewWidget()

    def resizePreviewWidget(self):
        geometry = self.titleWidget.geometry()
        self.previewWidget.setGeometry(
            geometry.x(),
            geometry.y() + self.titleWidget.height(),
            self.width() - 2 * geometry.x(),
            self.height() - 2 * geometry.y() - self.titleWidget.height())


if __name__ == "__main__":
    import sys
    import os
    os.chdir("../../")
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtGui import QFontDatabase
    app = QApplication(sys.argv)
    QFontDatabase.addApplicationFont("themes/default/font.ttf")
    w = SkinWidget()
    w.setStyleSheet(open("themes/default/style.qss",
                         "rb").read().decode("utf-8"))
    w.show()
    sys.exit(app.exec_())
