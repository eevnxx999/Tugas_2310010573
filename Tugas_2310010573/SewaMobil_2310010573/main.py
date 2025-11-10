# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from admin import form_Admin
from merek import form_Merek
from mobil import form_Mobil
from member import form_Member
from tawar import form_Tawar

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Sewa Mobil - Halaman Utama")
        filenya = QFile('main.ui')
        filenya.open(QFile.ReadOnly)
        muatfile = QUiLoader()
        self.formutama = muatfile.load(filenya,self)
        self.resize(self.formutama.size())
        self.setMenuBar(self.formutama.menuBar())

        self.formutama.actionData_Admin.triggered.connect(self.bukaAdmin)
        self.formutama.actionData_Merek.triggered.connect(self.bukaMerek)
        self.formutama.actionData_Mobil.triggered.connect(self.bukaMobil)
        self.formutama.actionData_Member.triggered.connect(self.bukaMember)
        self.formutama.actionData_Tawar.triggered.connect(self.bukaTawar)

    def bukaAdmin(self):
        self.formAdm = form_Admin()
        self.formAdm.show()

    def bukaMerek(self):
        self.formMer = form_Merek()
        self.formMer.show()

    def bukaMobil(self):
        self.formMob = form_Mobil()
        self.formMob.show()

    def bukaMember(self):
        self.formMem = form_Member()
        self.formMem.show()

    def bukaTawar(self):
        self.formTaw = form_Tawar()
        self.formTaw.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    jendela = MainWindow()
    jendela.show()
    sys.exit(app.exec())
