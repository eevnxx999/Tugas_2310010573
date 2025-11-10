# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'member.ui'
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
        Form.resize(522, 471)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(140, 60, 251, 341))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.idMemberLabel = QLabel(self.formLayoutWidget)
        self.idMemberLabel.setObjectName(u"idMemberLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.idMemberLabel)

        self.idMemberLineEdit = QLineEdit(self.formLayoutWidget)
        self.idMemberLineEdit.setObjectName(u"idMemberLineEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.idMemberLineEdit)

        self.usernameLabel = QLabel(self.formLayoutWidget)
        self.usernameLabel.setObjectName(u"usernameLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.usernameLabel)

        self.usernameLineEdit = QLineEdit(self.formLayoutWidget)
        self.usernameLineEdit.setObjectName(u"usernameLineEdit")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.usernameLineEdit)

        self.passwordLabel = QLabel(self.formLayoutWidget)
        self.passwordLabel.setObjectName(u"passwordLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.passwordLabel)

        self.passwordLineEdit = QLineEdit(self.formLayoutWidget)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.passwordLineEdit)

        self.BtnSimpan = QPushButton(self.formLayoutWidget)
        self.BtnSimpan.setObjectName(u"BtnSimpan")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.BtnSimpan)

        self.BtnUbah = QPushButton(self.formLayoutWidget)
        self.BtnUbah.setObjectName(u"BtnUbah")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.BtnUbah)

        self.BtnHapus = QPushButton(self.formLayoutWidget)
        self.BtnHapus.setObjectName(u"BtnHapus")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.LabelRole, self.BtnHapus)

        self.namaLabel = QLabel(self.formLayoutWidget)
        self.namaLabel.setObjectName(u"namaLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.namaLabel)

        self.namaLineEdit = QLineEdit(self.formLayoutWidget)
        self.namaLineEdit.setObjectName(u"namaLineEdit")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.namaLineEdit)

        self.alamatLabel = QLabel(self.formLayoutWidget)
        self.alamatLabel.setObjectName(u"alamatLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.alamatLabel)

        self.alamatLineEdit = QLineEdit(self.formLayoutWidget)
        self.alamatLineEdit.setObjectName(u"alamatLineEdit")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.alamatLineEdit)

        self.emailLabel = QLabel(self.formLayoutWidget)
        self.emailLabel.setObjectName(u"emailLabel")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.emailLabel)

        self.emailLineEdit = QLineEdit(self.formLayoutWidget)
        self.emailLineEdit.setObjectName(u"emailLineEdit")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.emailLineEdit)

        self.teleponLabel = QLabel(self.formLayoutWidget)
        self.teleponLabel.setObjectName(u"teleponLabel")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.teleponLabel)

        self.teleponLineEdit = QLineEdit(self.formLayoutWidget)
        self.teleponLineEdit.setObjectName(u"teleponLineEdit")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.teleponLineEdit)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.idMemberLabel.setText(QCoreApplication.translate("Form", u"Id Member", None))
        self.usernameLabel.setText(QCoreApplication.translate("Form", u"Username", None))
        self.passwordLabel.setText(QCoreApplication.translate("Form", u"Password", None))
        self.BtnSimpan.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
        self.BtnUbah.setText(QCoreApplication.translate("Form", u"UBAH", None))
        self.BtnHapus.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        self.namaLabel.setText(QCoreApplication.translate("Form", u"Nama", None))
        self.alamatLabel.setText(QCoreApplication.translate("Form", u"Alamat", None))
        self.emailLabel.setText(QCoreApplication.translate("Form", u"Email", None))
        self.teleponLabel.setText(QCoreApplication.translate("Form", u"Telepon", None))
    # retranslateUi

