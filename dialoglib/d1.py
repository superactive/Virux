# -*- coding: utf-8 -*-

#Virux, Platform bağımsız bir antivirüs yazılımıdır :P
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

from PyQt4.QtGui import QGridLayout, QLabel, QPushButton, QMessageBox
from basedialog import VDialog

class DMessage(VDialog):
    def __init__(self, parent):
        VDialog.__init__(self, parent)
        self.resize(450, 150)
        self.gLayout = QGridLayout(self)
        self.mesaj = QLabel(self)
        self.gLayout.addWidget(self.mesaj, 0, 0, 1, 3)
        self.pSil = QPushButton(self)
        self.pSil.setMinimumSize(100, 0)
        self.pSil.setMaximumSize(100, 25)
        self.gLayout.addWidget(self.pSil, 1, 0, 1, 1)
        self.pBirak = QPushButton(self)
        self.pBirak.setMinimumSize(100, 0)
        self.pBirak.setMaximumSize(100, 25)
        self.gLayout.addWidget(self.pBirak, 1, 2, 1, 1)
        self.pKarantina = QPushButton(self)
        self.pKarantina.setMinimumSize(100, 0)
        self.pKarantina.setMaximumSize(100, 25)
        self.gLayout.addWidget(self.pKarantina, 1, 1, 1, 1)

        self.pBirak.clicked.connect(self.birak)
        self.pKarantina.clicked.connect(self.karantina)
        self.pSil.clicked.connect(self.sil)

        self.setWindowTitle(u"Virüs Bulundu!")
        self.mesaj.setText(u"Zmanorka 816 Torsis B bulundu. İkinci derece tehlikleli bir trojan.<br>Sileyim mi, karantinaya mı alayım, bırakayım gitsin mi?")
        self.pSil.setText(u"Sil")
        self.pBirak.setText(u"Bırak Gitsin")
        self.pKarantina.setText(u"Karantinaya Al")

    def karantina(self):
        QMessageBox.information(self, u"Alamadım!", u"Tam karantinaya alırken kaçtı!", u"Afferin!")
        self.close()

    def sil(self):
        QMessageBox.information(self, u"Silinmiyor...", u"Silgim bitmiş :(", u"Hay Senin!")
        self.close()

    def birak(self):
        QMessageBox.information(self, u"Bırakmam!", u"Böylesi bulunmaz bir daha!", u"Bırak Lan!")
        QMessageBox.information(self, u"Bağırma!", u"Bağırma, adamı hasta etme!<br> Efendi ol canımı ye...", u"Özür dilerim!")
        self.close()

    @staticmethod
    def getOption():
        print "amk"