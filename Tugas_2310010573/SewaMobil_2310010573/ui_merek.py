# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'merek.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(566, 452)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(150, 70, 251, 281))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.BtnSimpan = QPushButton(self.formLayoutWidget)
        self.BtnSimpan.setObjectName(u"BtnSimpan")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.BtnSimpan)

        self.BtnUbah = QPushButton(self.formLayoutWidget)
        self.BtnUbah.setObjectName(u"BtnUbah")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.BtnUbah)

        self.BtnHapus = QPushButton(self.formLayoutWidget)
        self.BtnHapus.setObjectName(u"BtnHapus")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.BtnHapus)

        self.idMerekLabel = QLabel(self.formLayoutWidget)
        self.idMerekLabel.setObjectName(u"idMerekLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.idMerekLabel)

        self.idMerekLineEdit = QLineEdit(self.formLayoutWidget)
        self.idMerekLineEdit.setObjectName(u"idMerekLineEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.idMerekLineEdit)

        self.merekLabel = QLabel(self.formLayoutWidget)
        self.merekLabel.setObjectName(u"merekLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.merekLabel)

        self.merekLineEdit = QLineEdit(self.formLayoutWidget)
        self.merekLineEdit.setObjectName(u"merekLineEdit")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.merekLineEdit)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.BtnSimpan.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
        self.BtnUbah.setText(QCoreApplication.translate("Form", u"UBAH", None))
        self.BtnHapus.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        self.idMerekLabel.setText(QCoreApplication.translate("Form", u"Id Merek", None))
        self.merekLabel.setText(QCoreApplication.translate("Form", u"Merek", None))
    # retranslateUi

