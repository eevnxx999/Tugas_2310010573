# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mobil.ui'
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
        Form.resize(685, 648)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(220, 70, 251, 445))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.idMobilLabel = QLabel(self.formLayoutWidget)
        self.idMobilLabel.setObjectName(u"idMobilLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.idMobilLabel)

        self.idMobilLineEdit = QLineEdit(self.formLayoutWidget)
        self.idMobilLineEdit.setObjectName(u"idMobilLineEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.idMobilLineEdit)

        self.tanggalLabel = QLabel(self.formLayoutWidget)
        self.tanggalLabel.setObjectName(u"tanggalLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.tanggalLabel)

        self.tanggalDateEdit = QDateEdit(self.formLayoutWidget)
        self.tanggalDateEdit.setObjectName(u"tanggalDateEdit")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.tanggalDateEdit)

        self.idMerekLabel = QLabel(self.formLayoutWidget)
        self.idMerekLabel.setObjectName(u"idMerekLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.idMerekLabel)

        self.idMerekLineEdit = QLineEdit(self.formLayoutWidget)
        self.idMerekLineEdit.setObjectName(u"idMerekLineEdit")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.idMerekLineEdit)

        self.typeLabel = QLabel(self.formLayoutWidget)
        self.typeLabel.setObjectName(u"typeLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.typeLabel)

        self.typeLineEdit = QLineEdit(self.formLayoutWidget)
        self.typeLineEdit.setObjectName(u"typeLineEdit")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.typeLineEdit)

        self.tahunLabel = QLabel(self.formLayoutWidget)
        self.tahunLabel.setObjectName(u"tahunLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.tahunLabel)

        self.tahunLineEdit = QLineEdit(self.formLayoutWidget)
        self.tahunLineEdit.setObjectName(u"tahunLineEdit")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.tahunLineEdit)

        self.hargaLabel = QLabel(self.formLayoutWidget)
        self.hargaLabel.setObjectName(u"hargaLabel")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.hargaLabel)

        self.hargaLineEdit = QLineEdit(self.formLayoutWidget)
        self.hargaLineEdit.setObjectName(u"hargaLineEdit")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.hargaLineEdit)

        self.lokasiLabel = QLabel(self.formLayoutWidget)
        self.lokasiLabel.setObjectName(u"lokasiLabel")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.lokasiLabel)

        self.lokasiLineEdit = QLineEdit(self.formLayoutWidget)
        self.lokasiLineEdit.setObjectName(u"lokasiLineEdit")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.lokasiLineEdit)

        self.warnaLabel = QLabel(self.formLayoutWidget)
        self.warnaLabel.setObjectName(u"warnaLabel")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.warnaLabel)

        self.warnaLineEdit = QLineEdit(self.formLayoutWidget)
        self.warnaLineEdit.setObjectName(u"warnaLineEdit")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.warnaLineEdit)

        self.keteranganLineEdit = QLineEdit(self.formLayoutWidget)
        self.keteranganLineEdit.setObjectName(u"keteranganLineEdit")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.FieldRole, self.keteranganLineEdit)

        self.statusLabel = QLabel(self.formLayoutWidget)
        self.statusLabel.setObjectName(u"statusLabel")

        self.formLayout.setWidget(9, QFormLayout.ItemRole.LabelRole, self.statusLabel)

        self.statusLineEdit = QLineEdit(self.formLayoutWidget)
        self.statusLineEdit.setObjectName(u"statusLineEdit")

        self.formLayout.setWidget(9, QFormLayout.ItemRole.FieldRole, self.statusLineEdit)

        self.BtnSimpan = QPushButton(self.formLayoutWidget)
        self.BtnSimpan.setObjectName(u"BtnSimpan")

        self.formLayout.setWidget(10, QFormLayout.ItemRole.LabelRole, self.BtnSimpan)

        self.BtnUbah = QPushButton(self.formLayoutWidget)
        self.BtnUbah.setObjectName(u"BtnUbah")

        self.formLayout.setWidget(10, QFormLayout.ItemRole.FieldRole, self.BtnUbah)

        self.BtnHapus = QPushButton(self.formLayoutWidget)
        self.BtnHapus.setObjectName(u"BtnHapus")

        self.formLayout.setWidget(11, QFormLayout.ItemRole.LabelRole, self.BtnHapus)

        self.keteranganLabel = QLabel(self.formLayoutWidget)
        self.keteranganLabel.setObjectName(u"keteranganLabel")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.LabelRole, self.keteranganLabel)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.idMobilLabel.setText(QCoreApplication.translate("Form", u"Id Mobil", None))
        self.tanggalLabel.setText(QCoreApplication.translate("Form", u"Tanggal", None))
        self.idMerekLabel.setText(QCoreApplication.translate("Form", u"Id Merek", None))
        self.typeLabel.setText(QCoreApplication.translate("Form", u"Type", None))
        self.tahunLabel.setText(QCoreApplication.translate("Form", u"Tahun", None))
        self.hargaLabel.setText(QCoreApplication.translate("Form", u"Harga", None))
        self.lokasiLabel.setText(QCoreApplication.translate("Form", u"Lokasi", None))
        self.warnaLabel.setText(QCoreApplication.translate("Form", u"Warna", None))
        self.statusLabel.setText(QCoreApplication.translate("Form", u"Status", None))
        self.BtnSimpan.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
        self.BtnUbah.setText(QCoreApplication.translate("Form", u"UBAH", None))
        self.BtnHapus.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        self.keteranganLabel.setText(QCoreApplication.translate("Form", u"Keterangan", None))
    # retranslateUi

