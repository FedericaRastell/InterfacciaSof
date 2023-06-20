# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QListView, QListWidget, QListWidgetItem,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QToolBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1258, 684)
        self.actionzoom = QAction(MainWindow)
        self.actionzoom.setObjectName(u"actionzoom")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.open_folder = QPushButton(self.groupBox_2)
        self.open_folder.setObjectName(u"open_folder")

        self.verticalLayout.addWidget(self.open_folder)

        self.qlist_images = QListWidget(self.groupBox_2)
        self.qlist_images.setObjectName(u"qlist_images")
        self.qlist_images.setStyleSheet(u"background-color:white")
        self.qlist_images.setFrameShape(QFrame.Box)
        self.qlist_images.setFrameShadow(QFrame.Plain)
        self.qlist_images.setLayoutMode(QListView.Batched)
        self.qlist_images.setBatchSize(20)

        self.verticalLayout.addWidget(self.qlist_images)


        self.horizontalLayout_3.addWidget(self.groupBox_2)

        self.qlabel_image = QLabel(self.centralwidget)
        self.qlabel_image.setObjectName(u"qlabel_image")
        self.qlabel_image.setScaledContents(False)

        self.horizontalLayout_3.addWidget(self.qlabel_image)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.list_widget = QListWidget(self.groupBox)
        self.list_widget.setObjectName(u"list_widget")

        self.horizontalLayout_2.addWidget(self.list_widget)


        self.horizontalLayout_3.addWidget(self.groupBox)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 9)
        self.horizontalLayout_3.setStretch(2, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1258, 21))
        self.menufile = QMenu(self.menubar)
        self.menufile.setObjectName(u"menufile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menufile.menuAction())

        self.retranslateUi(MainWindow)
        self.open_folder.clicked.connect(MainWindow.selectDir)
        self.qlist_images.itemClicked.connect(MainWindow.item_click)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionzoom.setText(QCoreApplication.translate("MainWindow", u"zoom ", None))
        self.groupBox_2.setTitle("")
        self.open_folder.setText(QCoreApplication.translate("MainWindow", u"Open Folder", None))
        self.qlabel_image.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"AnnotationBox", None))
        self.menufile.setTitle(QCoreApplication.translate("MainWindow", u"file ", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

