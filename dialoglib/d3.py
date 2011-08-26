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

from PyQt4.QtGui import QDialog, QGridLayout, QLabel, QMessageBox, QPushButton, QSpacerItem, QSizePolicy
from PyQt4.QtCore import Qt

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

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            pass
