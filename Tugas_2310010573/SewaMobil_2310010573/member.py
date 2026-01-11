# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
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
        self.tampilDataMember()
        self.formMember.lineCari.textChanged.connect(self.cariDataMember)
        self.formMember.btnCetak.clicked.connect(self.laporanMember)

    def simpanMember(self):
            if not self.formMember.idMemberLineEdit.text().strip():
                QMessageBox.information(None, "Informasi", "ID Member belum diisi")
                self.formMember.idMemberLineEdit.setFocus()
            elif not self.formMember.usernameLineEdit.text().strip():
                QMessageBox.information(None, "Informasi", "Username belum diisi")
                self.formMember.usernameLineEdit.setFocus()
            elif not self.formMember.passwordLineEdit.text():
                QMessageBox.information(None, "Informasi", "Password belum diisi")
                self.formMember.passwordLineEdit.setFocus()
            elif not self.formMember.namaLineEdit.text().strip():
                QMessageBox.information(None, "Informasi", "Nama belum diisi")
                self.formMember.namaLineEdit.setFocus()
            else:
                id_member = self.formMember.idMemberLineEdit.text()
                username = self.formMember.usernameLineEdit.text()
                password = self.formMember.passwordLineEdit.text()
                nama = self.formMember.namaLineEdit.text()
                alamat = self.formMember.alamatLineEdit.text()
                email = self.formMember.emailLineEdit.text()
                telepon = self.formMember.teleponLineEdit.text()
                self.aksi.tambahMember(id_member, username, password, nama, alamat, email, telepon)

                self.tampilDataMember()
                QMessageBox.information(None, "Informasi", "Data Member berhasil disimpan")

    def ubahMember(self):
            id_member = self.formMember.idMemberLineEdit.text()
            username = self.formMember.usernameLineEdit.text()
            password = self.formMember.passwordLineEdit.text()
            nama = self.formMember.namaLineEdit.text()
            alamat = self.formMember.alamatLineEdit.text()
            email = self.formMember.emailLineEdit.text()
            telepon = self.formMember.teleponLineEdit.text()
            self.aksi.updateMember(id_member, username, password, nama, alamat, email, telepon)

            self.tampilDataMember()
            QMessageBox.information(None, "Informasi", "Data Member berhasil diubah")

    def hapusMember(self):
            pesan = QMessageBox.information(None, "Konfirmasi Hapus", "Apakah yakin menghapus data Member ini?",
            QMessageBox.Yes | QMessageBox.No)

            if pesan == QMessageBox.Yes:
                id_member = self.formMember.idMemberLineEdit.text()
                self.aksi.hapusMember(id_member)

                self.tampilDataMember()
                QMessageBox.information(None, "Informasi", "Data Member berhasil dihapus")
            else:
                pass

    def tampilDataMember(self):
            self.formMember.tblMember.setRowCount(0)
            data = self.aksi.dataMember() # Mengambil semua data member

            for i, baris in enumerate(data):
                self.formMember.tblMember.insertRow(i)
                self.formMember.tblMember.setItem(i, 0, QTableWidgetItem(str(baris["id_member"])))
                self.formMember.tblMember.setItem(i, 1, QTableWidgetItem(str(baris["username"])))
                self.formMember.tblMember.setItem(i, 2, QTableWidgetItem(str(baris["password"])))
                self.formMember.tblMember.setItem(i, 3, QTableWidgetItem(str(baris["nama"])))
                self.formMember.tblMember.setItem(i, 4, QTableWidgetItem(str(baris["alamat"])))
                self.formMember.tblMember.setItem(i, 5, QTableWidgetItem(str(baris["email"])))
                self.formMember.tblMember.setItem(i, 6, QTableWidgetItem(str(baris["telepon"])))

    def cariDataMember(self):
            varCari = self.formMember.lineCari.text()
            self.formMember.tblMember.setRowCount(0)
            data = self.aksi.filterMember(varCari) # Mengambil data member berdasarkan filter

            for i, baris in enumerate(data):
                self.formMember.tblMember.insertRow(i)
                self.formMember.tblMember.setItem(i, 0, QTableWidgetItem(str(baris["id_member"])))
                self.formMember.tblMember.setItem(i, 1, QTableWidgetItem(str(baris["username"])))
                self.formMember.tblMember.setItem(i, 2, QTableWidgetItem(str(baris["password"])))
                self.formMember.tblMember.setItem(i, 3, QTableWidgetItem(str(baris["nama"])))
                self.formMember.tblMember.setItem(i, 4, QTableWidgetItem(str(baris["alamat"])))
                self.formMember.tblMember.setItem(i, 5, QTableWidgetItem(str(baris["email"])))
                self.formMember.tblMember.setItem(i, 6, QTableWidgetItem(str(baris["telepon"])))

    def laporanMember(self):
            self.aksi.cetakMember()
