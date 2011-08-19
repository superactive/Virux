# -*- coding: utf-8 -*-
from PyQt4.QtGui import QDialog, QGridLayout, QLabel, QMessageBox, QPushButton, QSpacerItem, QSizePolicy

class DMessage(QDialog):
    def __init__(self, parent):
        QDialog.__init__(self, parent)
        self.resize(450, 150)
        self.gLayout = QGridLayout(self)
        self.mesaj = QLabel(self)
        self.gLayout.addWidget(self.mesaj, 0, 0, 1, 3)
        self.pGeliyor = QPushButton(self)
        self.pGeliyor.setMinimumSize(100, 0)
        self.gLayout.addWidget(self.pGeliyor, 1, 1, 1, 1)
        self.pHelal = QPushButton(self)
        self.pHelal.setMinimumSize(100, 0)
        self.gLayout.addWidget(self.pHelal, 1, 2, 1, 1)
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gLayout.addItem(spacerItem, 1, 0, 1, 1)

        self.pGeliyor.clicked.connect(self.geliyor)
        self.pHelal.clicked.connect(self.helal)

        self.setWindowTitle(u"Yardım Et!")
        self.mesaj.setText(u"Ölümcül bir virüs buldum ama o kadar güçlü ki baş edemiyorum.<br>Ya yardımıma bir iki antivirüs programı daha gönder ya da hakkını helal et!...")
        self.pGeliyor.setText(u"Geliyor abi!")
        self.pHelal.setText(u"Helal olsun!")

    def geliyor(self):
        QMessageBox.information(self, u"Yettim Gayri!", u"Yardıma geldik abi!", u"Afferin!")
        self.close()

    def helal(self):
        QMessageBox.information(self, u"Üzülme!", u"Her şeyin bir çaresi vardır!", u"Çare bul!")
        QMessageBox.information(self, u"Çare bulundu!", u"Her şeyin bir çaresi vardır demiştim!", u"Allah razı olsun!")
        self.close()

    def closeEvent(self, event):
        event.ignore()
        self.hide()