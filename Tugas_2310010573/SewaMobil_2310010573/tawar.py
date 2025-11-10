# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud_sewaMobil

class form_Tawar(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle("Sewa Mobil - Halaman Data Tawar")
        filenya = QFile('tawar.ui')
        filenya.open(QFile.ReadOnly)
        muatfile = QUiLoader()
        self.formTawar = muatfile.load(filenya,self)
        self.aksi = crud_sewaMobil()
        self.formTawar.BtnSimpan.clicked.connect(self.simpanTawar)
        self.formTawar.BtnUbah.clicked.connect(self.ubahTawar)
        self.formTawar.BtnHapus.clicked.connect(self.hapusTawar)

    def simpanTawar(self):
        id_pesan = self.formTawar.idPesanLineEdit.text()
        id_member = self.formTawar.idMemberLineEdit.text()
        id_mobil = self.formTawar.idMobilLineEdit.text()
        tawar = self.formTawar.tawarLineEdit.text()
        tanggal = self.formTawar.tanggalDateEdit.date().toString("yyyy-MM-dd")
        pesan = self.formTawar.pesanLineEdit.text()
        status = self.formTawar.statusLineEdit.text()

        self.aksi.tambahTawar(id_pesan, id_member, id_mobil, tawar, tanggal, pesan, status)

    def ubahTawar(self):
        id_pesan = self.formTawar.idPesanLineEdit.text()
        id_member = self.formTawar.idMemberLineEdit.text()
        id_mobil = self.formTawar.idMobilLineEdit.text()
        tawar = self.formTawar.tawarLineEdit.text()
        tanggal = self.formTawar.tanggalDateEdit.date().toString("yyyy-MM-dd")
        pesan = self.formTawar.pesanLineEdit.text()
        status = self.formTawar.statusLineEdit.text()

        self.aksi.updateTawar(id_pesan, id_member, id_mobil, tawar, tanggal, pesan, status)

    def hapusTawar(self):
        id_pesan = self.formTawar.idPesanLineEdit.text()
        self.aksi.hapusTawar(id_pesan)
