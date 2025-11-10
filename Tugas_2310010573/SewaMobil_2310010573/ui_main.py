# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionData_Admin = QAction(MainWindow)
        self.actionData_Admin.setObjectName(u"actionData_Admin")
        self.actionData_Merek = QAction(MainWindow)
        self.actionData_Merek.setObjectName(u"actionData_Merek")
        self.actionData_Mobil = QAction(MainWindow)
        self.actionData_Mobil.setObjectName(u"actionData_Mobil")
        self.actionData_Member = QAction(MainWindow)
        self.actionData_Member.setObjectName(u"actionData_Member")
        self.actionData_Tawar = QAction(MainWindow)
        self.actionData_Tawar.setObjectName(u"actionData_Tawar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 25))
        self.menuMenu_Utama = QMenu(self.menubar)
        self.menuMenu_Utama.setObjectName(u"menuMenu_Utama")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu_Utama.menuAction())
        self.menuMenu_Utama.addAction(self.actionData_Admin)
        self.menuMenu_Utama.addAction(self.actionData_Merek)
        self.menuMenu_Utama.addAction(self.actionData_Mobil)
        self.menuMenu_Utama.addAction(self.actionData_Member)
        self.menuMenu_Utama.addAction(self.actionData_Tawar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionData_Admin.setText(QCoreApplication.translate("MainWindow", u"Data Admin", None))
        self.actionData_Merek.setText(QCoreApplication.translate("MainWindow", u"Data Merek", None))
        self.actionData_Mobil.setText(QCoreApplication.translate("MainWindow", u"Data Mobil", None))
        self.actionData_Member.setText(QCoreApplication.translate("MainWindow", u"Data Member", None))
        self.actionData_Tawar.setText(QCoreApplication.translate("MainWindow", u"Data Tawar", None))
        self.menuMenu_Utama.setTitle(QCoreApplication.translate("MainWindow", u"Menu Utama", None))
    # retranslateUi

