# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud_sewaMobil

class form_Member(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle("Sewa Mobil - Halaman Data Member")
        filenya = QFile('member.ui')
        filenya.open(QFile.ReadOnly)
        muatfile = QUiLoader()
        self.formMember = muatfile.load(filenya,self)
        self.aksi = crud_sewaMobil()
        self.formMember.BtnSimpan.clicked.connect(self.simpanMember)
        self.formMember.BtnUbah.clicked.connect(self.ubahMember)
        self.formMember.BtnHapus.clicked.connect(self.hapusMember)

    def simpanMember(self):
        id_member = self.formMember.idMemberLineEdit.text()
        username = self.formMember.usernameLineEdit.text()
        password = self.formMember.passwordLineEdit.text()
        nama = self.formMember.namaLineEdit.text()
        alamat = self.formMember.alamatLineEdit.text()
        email = self.formMember.emailLineEdit.text()
        telepon = self.formMember.teleponLineEdit.text()

        self.aksi.tambahMember(id_member, username, password, nama, alamat, email, telepon)

    def ubahMember(self):
        id_member = self.formMember.idMemberLineEdit.text()
        username = self.formMember.usernameLineEdit.text()
        password = self.formMember.passwordLineEdit.text()
        nama = self.formMember.namaLineEdit.text()
        alamat = self.formMember.alamatLineEdit.text()
        email = self.formMember.emailLineEdit.text()
        telepon = self.formMember.teleponLineEdit.text()

        self.aksi.updateMember(id_member, username, password, nama, alamat, email, telepon)

    def hapusMember(self):
        id_member = self.formMember.idMemberLineEdit.text()
        self.aksi.hapusMember(id_member)
