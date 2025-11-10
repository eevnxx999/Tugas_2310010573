# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tawar.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QFormLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(526, 490)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(140, 100, 251, 313))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.BtnSimpan = QPushButton(self.formLayoutWidget)
        self.BtnSimpan.setObjectName(u"BtnSimpan")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.BtnSimpan)

        self.BtnUbah = QPushButton(self.formLayoutWidget)
        self.BtnUbah.setObjectName(u"BtnUbah")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.BtnUbah)

        self.BtnHapus = QPushButton(self.formLayoutWidget)
        self.BtnHapus.setObjectName(u"BtnHapus")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.LabelRole, self.BtnHapus)

        self.idPesanLabel = QLabel(self.formLayoutWidget)
        self.idPesanLabel.setObjectName(u"idPesanLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.idPesanLabel)

        self.idPesanLineEdit = QLineEdit(self.formLayoutWidget)
        self.idPesanLineEdit.setObjectName(u"idPesanLineEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.idPesanLineEdit)

        self.idMemberLabel = QLabel(self.formLayoutWidget)
        self.idMemberLabel.setObjectName(u"idMemberLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.idMemberLabel)

        self.idMemberLineEdit = QLineEdit(self.formLayoutWidget)
        self.idMemberLineEdit.setObjectName(u"idMemberLineEdit")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.idMemberLineEdit)

        self.idMobilLabel = QLabel(self.formLayoutWidget)
        self.idMobilLabel.setObjectName(u"idMobilLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.idMobilLabel)

        self.idMobilLineEdit = QLineEdit(self.formLayoutWidget)
        self.idMobilLineEdit.setObjectName(u"idMobilLineEdit")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.idMobilLineEdit)

        self.tawarLabel = QLabel(self.formLayoutWidget)
        self.tawarLabel.setObjectName(u"tawarLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.tawarLabel)

        self.tawarLineEdit = QLineEdit(self.formLayoutWidget)
        self.tawarLineEdit.setObjectName(u"tawarLineEdit")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.tawarLineEdit)

        self.tanggalLabel = QLabel(self.formLayoutWidget)
        self.tanggalLabel.setObjectName(u"tanggalLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.tanggalLabel)

        self.tanggalDateEdit = QDateEdit(self.formLayoutWidget)
        self.tanggalDateEdit.setObjectName(u"tanggalDateEdit")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.tanggalDateEdit)

        self.pesanLabel = QLabel(self.formLayoutWidget)
        self.pesanLabel.setObjectName(u"pesanLabel")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.pesanLabel)

        self.pesanLineEdit = QLineEdit(self.formLayoutWidget)
        self.pesanLineEdit.setObjectName(u"pesanLineEdit")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.pesanLineEdit)

        self.statusLabel = QLabel(self.formLayoutWidget)
        self.statusLabel.setObjectName(u"statusLabel")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.statusLabel)

        self.statusLineEdit = QLineEdit(self.formLayoutWidget)
        self.statusLineEdit.setObjectName(u"statusLineEdit")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.statusLineEdit)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.BtnSimpan.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
        self.BtnUbah.setText(QCoreApplication.translate("Form", u"UBAH", None))
        self.BtnHapus.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        self.idPesanLabel.setText(QCoreApplication.translate("Form", u"Id Pesan", None))
        self.idMemberLabel.setText(QCoreApplication.translate("Form", u"Id Member", None))
        self.idMobilLabel.setText(QCoreApplication.translate("Form", u"Id Mobil", None))
        self.tawarLabel.setText(QCoreApplication.translate("Form", u"Tawar", None))
        self.tanggalLabel.setText(QCoreApplication.translate("Form", u"Tanggal", None))
        self.pesanLabel.setText(QCoreApplication.translate("Form", u"Pesan", None))
        self.statusLabel.setText(QCoreApplication.translate("Form", u"Status", None))
    # retranslateUi

