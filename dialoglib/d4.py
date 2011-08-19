# -*- coding: utf-8 -*-

#Virux, GNU/Linux için bir antivirüs yazılımıdır :P
#Copyright (C) 2011, Metehan Özbek
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program. If not, see <http://www.gnu.org/licenses/>.

from PyQt4.QtGui import QDialog, QGridLayout, QLabel, QPushButton, QSpacerItem, QSizePolicy, QMessageBox

class DMessage(QDialog):
    def __init__(self, parent):
        QDialog.__init__(self, parent)
        self.resize(450, 150)
        self.gLayout = QGridLayout(self)
        self.mesaj = QLabel(self)
        self.gLayout.addWidget(self.mesaj, 0, 0, 1, 3)
        self.pDaha = QPushButton(self)
        self.gLayout.addWidget(self.pDaha, 1, 1, 1, 1)
        self.pUzulme = QPushButton(self)
        self.gLayout.addWidget(self.pUzulme, 1, 2, 1, 1)
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gLayout.addItem(spacerItem, 1, 0, 1, 1)

        self.pDaha.clicked.connect(self.daha)
        self.pUzulme.clicked.connect(self.close)

        self.setWindowTitle(u"Hay Aksi!")
        self.mesaj.setText(u"Hay Aksi! Elimden kaçırdım bir tane...")
        self.pDaha.setText(u"Daha dikkatli ol!")
        self.pUzulme.setText(u"Üzülme be abi")

    def daha(self):
        QMessageBox.information(self, u"Emredersiniz!", u"Emredersiniz Paşam!", u"Uzatma!")
        self.close()

    def closeEvent(self, event):
        event.ignore()
        self.hide()