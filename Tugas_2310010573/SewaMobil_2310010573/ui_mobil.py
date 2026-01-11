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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFormLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1004, 714)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(110, 70, 251, 441))
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

        self.keteranganLabel = QLabel(self.formLayoutWidget)
        self.keteranganLabel.setObjectName(u"keteranganLabel")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.LabelRole, self.keteranganLabel)

        self.keteranganLineEdit = QLineEdit(self.formLayoutWidget)
        self.keteranganLineEdit.setObjectName(u"keteranganLineEdit")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.FieldRole, self.keteranganLineEdit)

        self.statusLabel = QLabel(self.formLayoutWidget)
        self.statusLabel.setObjectName(u"statusLabel")

        self.formLayout.setWidget(9, QFormLayout.ItemRole.LabelRole, self.statusLabel)

        self.BtnSimpan = QPushButton(self.formLayoutWidget)
        self.BtnSimpan.setObjectName(u"BtnSimpan")

        self.formLayout.setWidget(11, QFormLayout.ItemRole.LabelRole, self.BtnSimpan)

        self.BtnUbah = QPushButton(self.formLayoutWidget)
        self.BtnUbah.setObjectName(u"BtnUbah")

        self.formLayout.setWidget(11, QFormLayout.ItemRole.FieldRole, self.BtnUbah)

        self.BtnHapus = QPushButton(self.formLayoutWidget)
        self.BtnHapus.setObjectName(u"BtnHapus")

        self.formLayout.setWidget(12, QFormLayout.ItemRole.LabelRole, self.BtnHapus)

        self.statusComboBox = QComboBox(self.formLayoutWidget)
        self.statusComboBox.addItem("")
        self.statusComboBox.addItem("")
        self.statusComboBox.setObjectName(u"statusComboBox")

        self.formLayout.setWidget(9, QFormLayout.ItemRole.FieldRole, self.statusComboBox)

        self.lineCari = QLineEdit(Form)
        self.lineCari.setObjectName(u"lineCari")
        self.lineCari.setGeometry(QRect(410, 70, 491, 28))
        self.tblMobil = QTableWidget(Form)
        if (self.tblMobil.columnCount() < 10):
            self.tblMobil.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblMobil.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblMobil.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblMobil.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblMobil.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblMobil.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tblMobil.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tblMobil.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tblMobil.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tblMobil.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tblMobil.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.tblMobil.setObjectName(u"tblMobil")
        self.tblMobil.setGeometry(QRect(400, 130, 501, 381))
        self.formLayoutWidget_2 = QWidget(Form)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(110, 540, 791, 111))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.filterDataLabel = QLabel(self.formLayoutWidget_2)
        self.filterDataLabel.setObjectName(u"filterDataLabel")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.filterDataLabel)

        self.comboFilter = QComboBox(self.formLayoutWidget_2)
        self.comboFilter.addItem("")
        self.comboFilter.addItem("")
        self.comboFilter.setObjectName(u"comboFilter")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.comboFilter)

        self.btnCetak = QPushButton(self.formLayoutWidget_2)
        self.btnCetak.setObjectName(u"btnCetak")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.btnCetak)

        self.comboStatus = QComboBox(self.formLayoutWidget_2)
        self.comboStatus.addItem("")
        self.comboStatus.addItem("")
        self.comboStatus.setObjectName(u"comboStatus")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.comboStatus)

        self.statusLabel_2 = QLabel(self.formLayoutWidget_2)
        self.statusLabel_2.setObjectName(u"statusLabel_2")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.statusLabel_2)


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
        self.keteranganLabel.setText(QCoreApplication.translate("Form", u"Keterangan", None))
        self.statusLabel.setText(QCoreApplication.translate("Form", u"Status", None))
        self.BtnSimpan.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
        self.BtnUbah.setText(QCoreApplication.translate("Form", u"UBAH", None))
        self.BtnHapus.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        self.statusComboBox.setItemText(0, QCoreApplication.translate("Form", u"Tersedia", None))
        self.statusComboBox.setItemText(1, QCoreApplication.translate("Form", u"Disewakan", None))

        ___qtablewidgetitem = self.tblMobil.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Id Mobil", None));
        ___qtablewidgetitem1 = self.tblMobil.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Tanggal", None));
        ___qtablewidgetitem2 = self.tblMobil.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Id Merek", None));
        ___qtablewidgetitem3 = self.tblMobil.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Type", None));
        ___qtablewidgetitem4 = self.tblMobil.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Tahun", None));
        ___qtablewidgetitem5 = self.tblMobil.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Harga", None));
        ___qtablewidgetitem6 = self.tblMobil.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"Lokasi", None));
        ___qtablewidgetitem7 = self.tblMobil.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"Warna", None));
        ___qtablewidgetitem8 = self.tblMobil.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"Keterangan", None));
        ___qtablewidgetitem9 = self.tblMobil.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"Status", None));
        self.filterDataLabel.setText(QCoreApplication.translate("Form", u"Filter Data", None))
        self.comboFilter.setItemText(0, QCoreApplication.translate("Form", u"Semua", None))
        self.comboFilter.setItemText(1, QCoreApplication.translate("Form", u"Status", None))

        self.btnCetak.setText(QCoreApplication.translate("Form", u"Cetak", None))
        self.comboStatus.setItemText(0, QCoreApplication.translate("Form", u"Tersedia", None))
        self.comboStatus.setItemText(1, QCoreApplication.translate("Form", u"Disewakan", None))

        self.statusLabel_2.setText(QCoreApplication.translate("Form", u"Status", None))
    # retranslateUi

