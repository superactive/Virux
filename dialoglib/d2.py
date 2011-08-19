# -*- coding: utf-8 -*-
from PyQt4.QtGui import QDialog, QGridLayout, QLabel, QPushButton, QMessageBox, QSpacerItem, QSizePolicy

class DMessage(QDialog):
    def __init__(self, parent):
        QDialog.__init__(self, parent)
        self.resize(450, 150)
        self.gLayout = QGridLayout(self)
        self.mesaj = QLabel(self)
        self.gLayout.addWidget(self.mesaj, 0, 0, 1, 3)
        self.pYapma = QPushButton(self)
        self.gLayout.addWidget(self.pYapma, 1, 2, 1, 1)
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.pSifirlama = QPushButton(self)
        self.pSifirlama.setEnabled(False)
        self.gLayout.addWidget(self.pSifirlama, 1, 1, 1, 1)

        self.pYapma.clicked.connect(self.yapma)

        self.setWindowTitle(u"Eyvah!")
        self.mesaj.setText(u"Virux, sistemin tamamını virüs olarak algıladı. Sistem sıfırlanıyor.")
        self.pYapma.setText(u"Yapma be abi!")
        self.pSifirlama.setText(u"Sıfırlama!")

    def yapma(self):
        QMessageBox.information(self, u":)", u"Yaptım bile!", u"Öyle olsun :(")
        self.close()

    def closeEvent(self, event):
        event.ignore()
        self.hide()