# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QApplication, QWidget
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

    def simpanMerek(self):
            id_merek = self.formMerek.idMerekLineEdit.text()
            merek = self.formMerek.merekLineEdit.text()
            self.aksi.tambahMerek(id_merek, merek)

    def ubahMerek(self):
        id_merek = self.formMerek.idMerekLineEdit.text()
        merek = self.formMerek.merekLineEdit.text()
        self.aksi.updateMerek(id_merek, merek)

    def hapusMerek(self):
        id_merek = self.formMerek.idMerekLineEdit.text()
        self.aksi.hapusMerek(id_merek)
