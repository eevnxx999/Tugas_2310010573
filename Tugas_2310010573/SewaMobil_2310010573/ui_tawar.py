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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFormLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(915, 651)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(140, 100, 251, 313))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
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

        self.BtnSimpan = QPushButton(self.formLayoutWidget)
        self.BtnSimpan.setObjectName(u"BtnSimpan")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.BtnSimpan)

        self.BtnUbah = QPushButton(self.formLayoutWidget)
        self.BtnUbah.setObjectName(u"BtnUbah")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.BtnUbah)

        self.BtnHapus = QPushButton(self.formLayoutWidget)
        self.BtnHapus.setObjectName(u"BtnHapus")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.LabelRole, self.BtnHapus)

        self.statusLabel = QLabel(self.formLayoutWidget)
        self.statusLabel.setObjectName(u"statusLabel")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.statusLabel)

        self.statusComboBox = QComboBox(self.formLayoutWidget)
        self.statusComboBox.addItem("")
        self.statusComboBox.addItem("")
        self.statusComboBox.addItem("")
        self.statusComboBox.setObjectName(u"statusComboBox")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.statusComboBox)

        self.lineCari = QLineEdit(Form)
        self.lineCari.setObjectName(u"lineCari")
        self.lineCari.setGeometry(QRect(430, 100, 371, 28))
        self.tblTawar = QTableWidget(Form)
        if (self.tblTawar.columnCount() < 7):
            self.tblTawar.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblTawar.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblTawar.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblTawar.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblTawar.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblTawar.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tblTawar.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tblTawar.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tblTawar.setObjectName(u"tblTawar")
        self.tblTawar.setGeometry(QRect(430, 160, 371, 251))
        self.formLayoutWidget_2 = QWidget(Form)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(140, 430, 661, 111))
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
        self.idPesanLabel.setText(QCoreApplication.translate("Form", u"Id Pesan", None))
        self.idMemberLabel.setText(QCoreApplication.translate("Form", u"Id Member", None))
        self.idMobilLabel.setText(QCoreApplication.translate("Form", u"Id Mobil", None))
        self.tawarLabel.setText(QCoreApplication.translate("Form", u"Tawar", None))
        self.tanggalLabel.setText(QCoreApplication.translate("Form", u"Tanggal", None))
        self.pesanLabel.setText(QCoreApplication.translate("Form", u"Pesan", None))
        self.BtnSimpan.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
        self.BtnUbah.setText(QCoreApplication.translate("Form", u"UBAH", None))
        self.BtnHapus.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        self.statusLabel.setText(QCoreApplication.translate("Form", u"Status", None))
        self.statusComboBox.setItemText(0, QCoreApplication.translate("Form", u"Pending", None))
        self.statusComboBox.setItemText(1, QCoreApplication.translate("Form", u"Diterima", None))
        self.statusComboBox.setItemText(2, QCoreApplication.translate("Form", u"Ditolak", None))

        ___qtablewidgetitem = self.tblTawar.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Id Pesan", None));
        ___qtablewidgetitem1 = self.tblTawar.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Id Member", None));
        ___qtablewidgetitem2 = self.tblTawar.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Id Mobil", None));
        ___qtablewidgetitem3 = self.tblTawar.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Tawar", None));
        ___qtablewidgetitem4 = self.tblTawar.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Tanggal", None));
        ___qtablewidgetitem5 = self.tblTawar.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Pesan", None));
        ___qtablewidgetitem6 = self.tblTawar.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"Status", None));
        self.filterDataLabel.setText(QCoreApplication.translate("Form", u"Filter Data", None))
        self.comboFilter.setItemText(0, QCoreApplication.translate("Form", u"Semua", None))
        self.comboFilter.setItemText(1, QCoreApplication.translate("Form", u"Status", None))

        self.btnCetak.setText(QCoreApplication.translate("Form", u"Cetak", None))
        self.comboStatus.setItemText(0, QCoreApplication.translate("Form", u"Pending", None))
        self.comboStatus.setItemText(1, QCoreApplication.translate("Form", u"Diterima", None))
        self.comboStatus.setItemText(2, QCoreApplication.translate("Form", u"Ditolak", None))

        self.statusLabel_2.setText(QCoreApplication.translate("Form", u"Status", None))
    # retranslateUi

