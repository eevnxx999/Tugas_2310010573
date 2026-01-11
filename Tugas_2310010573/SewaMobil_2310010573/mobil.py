# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud_sewaMobil

class form_Mobil(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle("Sewa Mobil - Halaman Data Mobil")
        filenya = QFile('mobil.ui')
        filenya.open(QFile.ReadOnly)
        muatfile = QUiLoader()
        self.formMobil = muatfile.load(filenya,self)
        self.aksi = crud_sewaMobil()
        self.formMobil.BtnSimpan.clicked.connect(self.simpanMobil)
        self.formMobil.BtnUbah.clicked.connect(self.ubahMobil)
        self.formMobil.BtnHapus.clicked.connect(self.hapusMobil)
        self.tampilDataMobil()
        self.formMobil.lineCari.textChanged.connect(self.cariDataMobil)
        self.formMobil.btnCetak.clicked.connect(self.laporanMobil)

    def simpanMobil(self):
            if not self.formMobil.idMobilLineEdit.text().strip():
                QMessageBox.information(None, "Informasi", "ID Mobil belum diisi")
                self.formMobil.idMobilLineEdit.setFocus()
            elif not self.formMobil.typeLineEdit.text().strip():
                QMessageBox.information(None, "Informasi", "Tipe Mobil belum diisi")
                self.formMobil.typeLineEdit.setFocus()
            else:
                id_mobil = self.formMobil.idMobilLineEdit.text()
                tanggal = self.formMobil.tanggalDateEdit.date().toString("yyyy-MM-dd")
                id_merek = self.formMobil.idMerekLineEdit.text()
                type_mobil = self.formMobil.typeLineEdit.text()
                tahun = self.formMobil.tahunLineEdit.text()
                harga = self.formMobil.hargaLineEdit.text()
                lokasi = self.formMobil.lokasiLineEdit.text()
                warna = self.formMobil.warnaLineEdit.text()
                keterangan = self.formMobil.keteranganLineEdit.text()
                status = self.formMobil.statusComboBox.currentText()

                self.aksi.tambahMobil(
                    id_mobil, tanggal, id_merek, type_mobil, tahun,
                    harga, lokasi, warna, keterangan, status
                )

                self.tampilDataMobil()
                QMessageBox.information(None, "Informasi", "Data Mobil berhasil disimpan")

    def ubahMobil(self):
            id_mobil = self.formMobil.idMobilLineEdit.text()
            tanggal = self.formMobil.tanggalDateEdit.date().toString("yyyy-MM-dd")
            id_merek = self.formMobil.idMerekLineEdit.text()
            type_mobil = self.formMobil.typeLineEdit.text()
            tahun = self.formMobil.tahunLineEdit.text()
            harga = self.formMobil.hargaLineEdit.text()
            lokasi = self.formMobil.lokasiLineEdit.text()
            warna = self.formMobil.warnaLineEdit.text()
            keterangan = self.formMobil.keteranganLineEdit.text()
            status = self.formMobil.statusComboBox.currentText()

            self.aksi.updateMobil(
                id_mobil, tanggal, id_merek, type_mobil, tahun,
                harga, lokasi, warna, keterangan, status
            )

            self.tampilDataMobil()
            QMessageBox.information(None, "Informasi", "Data Mobil berhasil diubah")

    def hapusMobil(self):
            pesan = QMessageBox.information(None, "Konfirmasi Hapus", "Apakah yakin menghapus data Mobil ini?",
            QMessageBox.Yes | QMessageBox.No)

            if pesan == QMessageBox.Yes:
                id_mobil = self.formMobil.idMobilLineEdit.text()
                self.aksi.hapusMobil(id_mobil)

                self.tampilDataMobil()
                QMessageBox.information(None, "Informasi", "Data Mobil berhasil dihapus")
            else:
                pass

    def tampilDataMobil(self):
            self.formMobil.tblMobil.setRowCount(0)
            data = self.aksi.dataMobil()

            for i, baris in enumerate(data):
                self.formMobil.tblMobil.insertRow(i)
                self.formMobil.tblMobil.setItem(i, 0, QTableWidgetItem(str(baris["id_mobil"])))
                self.formMobil.tblMobil.setItem(i, 1, QTableWidgetItem(str(baris["tanggal"])))
                self.formMobil.tblMobil.setItem(i, 2, QTableWidgetItem(str(baris["id_merek"])))
                self.formMobil.tblMobil.setItem(i, 3, QTableWidgetItem(str(baris["type"])))
                self.formMobil.tblMobil.setItem(i, 4, QTableWidgetItem(str(baris["tahun"])))
                self.formMobil.tblMobil.setItem(i, 5, QTableWidgetItem(str(baris["harga"])))
                self.formMobil.tblMobil.setItem(i, 6, QTableWidgetItem(str(baris["lokasi"])))
                self.formMobil.tblMobil.setItem(i, 7, QTableWidgetItem(str(baris["warna"])))
                self.formMobil.tblMobil.setItem(i, 8, QTableWidgetItem(str(baris["keterangan"])))
                self.formMobil.tblMobil.setItem(i, 9, QTableWidgetItem(str(baris["status"])))

    def cariDataMobil(self):
            varCari = self.formMobil.lineCari.text()
            self.formMobil.tblMobil.setRowCount(0)
            data = self.aksi.filterMobil(varCari)

            for i, baris in enumerate(data):
                self.formMobil.tblMobil.insertRow(i)
                self.formMobil.tblMobil.setItem(i, 0, QTableWidgetItem(str(baris["id_mobil"])))
                self.formMobil.tblMobil.setItem(i, 1, QTableWidgetItem(str(baris["tanggal"])))
                self.formMobil.tblMobil.setItem(i, 2, QTableWidgetItem(str(baris["id_merek"])))
                self.formMobil.tblMobil.setItem(i, 3, QTableWidgetItem(str(baris["type"])))
                self.formMobil.tblMobil.setItem(i, 4, QTableWidgetItem(str(baris["tahun"])))
                self.formMobil.tblMobil.setItem(i, 5, QTableWidgetItem(str(baris["harga"])))
                self.formMobil.tblMobil.setItem(i, 6, QTableWidgetItem(str(baris["lokasi"])))
                self.formMobil.tblMobil.setItem(i, 7, QTableWidgetItem(str(baris["warna"])))
                self.formMobil.tblMobil.setItem(i, 8, QTableWidgetItem(str(baris["keterangan"])))
                self.formMobil.tblMobil.setItem(i, 9, QTableWidgetItem(str(baris["status"])))

    def laporanMobil(self):
            cari = self.formMobil.comboStatus.currentText()
            filter = self.formMobil.comboFilter.currentText()
            if filter == "Semua" :
                self.aksi.cetakMobil()
            else:
                self.aksi.cetakFilterMobil(cari)
