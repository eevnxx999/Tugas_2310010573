# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
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
        self.tampilDataTawar()
        self.formTawar.lineCari.textChanged.connect(self.cariDataTawar)
        self.formTawar.btnCetak.clicked.connect(self.laporanTawar)

    def simpanTawar(self):
            if not self.formTawar.idPesanLineEdit.text().strip():
                QMessageBox.information(None, "Informasi", "ID Pesan belum diisi")
                self.formTawar.idPesanLineEdit.setFocus()
            elif not self.formTawar.idMemberLineEdit.text().strip():
                QMessageBox.information(None, "Informasi", "ID Member belum diisi")
                self.formTawar.idMemberLineEdit.setFocus()
            elif not self.formTawar.idMobilLineEdit.text().strip():
                QMessageBox.information(None, "Informasi", "ID Mobil belum diisi")
                self.formTawar.idMobilLineEdit.setFocus()
            else:
                id_pesan = self.formTawar.idPesanLineEdit.text()
                id_member = self.formTawar.idMemberLineEdit.text()
                id_mobil = self.formTawar.idMobilLineEdit.text()
                tawar = self.formTawar.tawarLineEdit.text()
                tanggal = self.formTawar.tanggalDateEdit.date().toString("yyyy-MM-dd")
                pesan = self.formTawar.pesanLineEdit.text()
                status = self.formTawar.statusComboBox.currentText()
                self.aksi.tambahTawar(id_pesan, id_member, id_mobil, tawar, tanggal, pesan, status)

                self.tampilDataTawar()
                QMessageBox.information(None, "Informasi", "Data Tawar berhasil disimpan")

    def ubahTawar(self):
            id_pesan = self.formTawar.idPesanLineEdit.text()
            id_member = self.formTawar.idMemberLineEdit.text()
            id_mobil = self.formTawar.idMobilLineEdit.text()
            tawar = self.formTawar.tawarLineEdit.text()
            tanggal = self.formTawar.tanggalDateEdit.date().toString("yyyy-MM-dd")
            pesan = self.formTawar.pesanLineEdit.text()
            status = self.formTawar.statusComboBox.currentText()
            self.aksi.updateTawar(id_pesan, id_member, id_mobil, tawar, tanggal, pesan, status)

            self.tampilDataTawar()
            QMessageBox.information(None, "Informasi", "Data Tawar berhasil diubah")

    def hapusTawar(self):
            pesan = QMessageBox.information(None, "Konfirmasi Hapus","Apakah yakin menghapus data Tawar/Pesan ini?",
            QMessageBox.Yes | QMessageBox.No)

            if pesan == QMessageBox.Yes:
                id_pesan = self.formTawar.idPesanLineEdit.text()
                self.aksi.hapusTawar(id_pesan)

                self.tampilDataTawar()
                QMessageBox.information(None, "Informasi", "Data Tawar berhasil dihapus")
            else:
                pass

    def tampilDataTawar(self):
            self.formTawar.tblTawar.setRowCount(0)
            data = self.aksi.dataTawar() # Mengambil semua data tawar

            for i, baris in enumerate(data):
                self.formTawar.tblTawar.insertRow(i)
                self.formTawar.tblTawar.setItem(i, 0, QTableWidgetItem(str(baris["id_pesan"])))
                self.formTawar.tblTawar.setItem(i, 1, QTableWidgetItem(str(baris["id_member"])))
                self.formTawar.tblTawar.setItem(i, 2, QTableWidgetItem(str(baris["id_mobil"])))
                self.formTawar.tblTawar.setItem(i, 3, QTableWidgetItem(str(baris["tawar"])))
                self.formTawar.tblTawar.setItem(i, 4, QTableWidgetItem(str(baris["tanggal"])))
                self.formTawar.tblTawar.setItem(i, 5, QTableWidgetItem(str(baris["pesan"])))
                self.formTawar.tblTawar.setItem(i, 6, QTableWidgetItem(str(baris["status"])))

    def cariDataTawar(self):
            varCari = self.formTawar.lineCari.text()
            self.formTawar.tblTawar.setRowCount(0)
            data = self.aksi.filterTawar(varCari) # Mengambil data tawar berdasarkan filter

            for i, baris in enumerate(data):
                self.formTawar.tblTawar.insertRow(i)
                self.formTawar.tblTawar.setItem(i, 0, QTableWidgetItem(str(baris["id_pesan"])))
                self.formTawar.tblTawar.setItem(i, 1, QTableWidgetItem(str(baris["id_member"])))
                self.formTawar.tblTawar.setItem(i, 2, QTableWidgetItem(str(baris["id_mobil"])))
                self.formTawar.tblTawar.setItem(i, 3, QTableWidgetItem(str(baris["tawar"])))
                self.formTawar.tblTawar.setItem(i, 4, QTableWidgetItem(str(baris["tanggal"])))
                self.formTawar.tblTawar.setItem(i, 5, QTableWidgetItem(str(baris["pesan"])))
                self.formTawar.tblTawar.setItem(i, 6, QTableWidgetItem(str(baris["status"])))

    def laporanTawar(self):
            cari = self.formTawar.comboStatus.currentText()
            filter = self.formTawar.comboFilter.currentText()
            if filter == "Semua" :
                self.aksi.cetakTawar()
            else:
                self.aksi.cetakFilterTawar(cari)
