# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QApplication, QWidget
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

    def simpanMobil(self):
            id_mobil = self.formMobil.idMobilLineEdit.text()
            tanggal = self.formMobil.tanggalDateEdit.date().toString("yyyy-MM-dd")
            id_merek = self.formMobil.idMerekLineEdit.text()
            type_mobil = self.formMobil.typeLineEdit.text()
            tahun = self.formMobil.tahunLineEdit.text()
            harga = self.formMobil.hargaLineEdit.text()
            lokasi = self.formMobil.lokasiLineEdit.text()
            warna = self.formMobil.warnaLineEdit.text()
            keterangan = self.formMobil.keteranganLineEdit.text()
            status = self.formMobil.statusLineEdit.text()

            self.aksi.tambahMobil(
                id_mobil, tanggal, id_merek, type_mobil, tahun,
                harga, lokasi, warna, keterangan, status
            )

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
        status = self.formMobil.statusLineEdit.text()

        self.aksi.updateMobil(
            id_mobil, tanggal, id_merek, type_mobil, tahun,
            harga, lokasi, warna, keterangan, status
        )

    def hapusMobil(self):
        id_mobil = self.formMobil.idMobilLineEdit.text()
        self.aksi.hapusMobil(id_mobil)
