# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud_sewaMobil

class form_Merek(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle("Sewa Mobil - Halaman Data Merek")
        filenya = QFile('merek.ui')
        filenya.open(QFile.ReadOnly)
        muatfile = QUiLoader()
        self.formMerek = muatfile.load(filenya,self)
        self.aksi = crud_sewaMobil()
        self.formMerek.BtnSimpan.clicked.connect(self.simpanMerek)
        self.formMerek.BtnUbah.clicked.connect(self.ubahMerek)
        self.formMerek.BtnHapus.clicked.connect(self.hapusMerek)
        self.tampilDataMerek()
        self.formMerek.lineCari.textChanged.connect(self.cariDataMerek)
        self.formMerek.btnCetak.clicked.connect(self.laporanMerek)

    def simpanMerek(self):
            if not self.formMerek.idMerekLineEdit.text().strip():
                QMessageBox.information(None, "Informasi", "ID Merek belum diisi")
                self.formMerek.idMerekLineEdit.setFocus()
            elif not self.formMerek.merekLineEdit.text().strip():
                QMessageBox.information(None, "Informasi", "Nama Merek belum diisi")
                self.formMerek.merekLineEdit.setFocus()
            else:
                id_merek = self.formMerek.idMerekLineEdit.text()
                merek = self.formMerek.merekLineEdit.text()

                self.aksi.tambahMerek(id_merek, merek)

                self.tampilDataMerek()
                QMessageBox.information(None, "Informasi", "Data Merek berhasil disimpan")

    def ubahMerek(self):
            id_merek = self.formMerek.idMerekLineEdit.text()
            merek = self.formMerek.merekLineEdit.text()
            self.aksi.updateMerek(id_merek, merek)

            self.tampilDataMerek()
            QMessageBox.information(None, "Informasi", "Data Merek berhasil diubah")

    def hapusMerek(self):
            pesan = QMessageBox.information(None, "Konfirmasi Hapus", "Apakah yakin menghapus data Merek ini?",
            QMessageBox.Yes | QMessageBox.No)

            if pesan == QMessageBox.Yes:
                id_merek = self.formMerek.idMerekLineEdit.text()
                self.aksi.hapusMerek(id_merek)

                self.tampilDataMerek()
                QMessageBox.information(None, "Informasi", "Data Merek berhasil dihapus")
            else:
                pass

    def tampilDataMerek(self):
            self.formMerek.tblMerek.setRowCount(0)
            data = self.aksi.dataMerek()

            for i, baris in enumerate(data):
                self.formMerek.tblMerek.insertRow(i)
                self.formMerek.tblMerek.setItem(i, 0, QTableWidgetItem(str(baris["id_merek"])))
                self.formMerek.tblMerek.setItem(i, 1, QTableWidgetItem(str(baris["merek"])))

    def cariDataMerek(self):
            varCari = self.formMerek.lineCari.text()
            self.formMerek.tblMerek.setRowCount(0)
            data = self.aksi.filterMerek(varCari)

            for i, baris in enumerate(data):
                self.formMerek.tblMerek.insertRow(i)
                self.formMerek.tblMerek.setItem(i, 0, QTableWidgetItem(str(baris["id_merek"])))
                self.formMerek.tblMerek.setItem(i, 1, QTableWidgetItem(str(baris["merek"])))

    def laporanMerek(self):
            cari = self.formMerek.txtMerek.text()
            filter = self.formMerek.comboFilter.currentText()
            if filter == "Semua" :
                self.aksi.cetakMerek()
            else:
                self.aksi.cetakFilterMerek(cari)
