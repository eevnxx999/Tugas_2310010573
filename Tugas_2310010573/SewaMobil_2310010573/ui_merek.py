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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(835, 561)
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

        self.lineCari = QLineEdit(Form)
        self.lineCari.setObjectName(u"lineCari")
        self.lineCari.setGeometry(QRect(440, 70, 261, 28))
        self.tblMerek = QTableWidget(Form)
        if (self.tblMerek.columnCount() < 2):
            self.tblMerek.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblMerek.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblMerek.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tblMerek.setObjectName(u"tblMerek")
        self.tblMerek.setGeometry(QRect(440, 130, 261, 221))
        self.formLayoutWidget_2 = QWidget(Form)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(150, 370, 551, 111))
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

        self.txtMerek = QLineEdit(self.formLayoutWidget_2)
        self.txtMerek.setObjectName(u"txtMerek")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtMerek)


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
        ___qtablewidgetitem = self.tblMerek.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Id Merek", None));
        ___qtablewidgetitem1 = self.tblMerek.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Merek", None));
        self.filterDataLabel.setText(QCoreApplication.translate("Form", u"Filter Data", None))
        self.comboFilter.setItemText(0, QCoreApplication.translate("Form", u"Semua", None))
        self.comboFilter.setItemText(1, QCoreApplication.translate("Form", u"Merek", None))

        self.btnCetak.setText(QCoreApplication.translate("Form", u"Cetak", None))
    # retranslateUi

