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

from PyQt4.QtGui import QDialog, QGridLayout, QLabel, QPushButton, QMessageBox, QSpacerItem, QSizePolicy
from PyQt4.QtCore import Qt

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

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            pass
