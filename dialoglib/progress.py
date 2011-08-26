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

from PyQt4.QtGui import QDialog, QPushButton, QGridLayout, QLabel, QProgressBar, QSpacerItem, QSizePolicy, QMessageBox
from PyQt4.QtCore import Qt, QBasicTimer
import os, sys

class DMessage(QDialog):
    def __init__(self, parent):
        QDialog.__init__(self, parent)
        self.resize(450, 150)
        self.setMinimumSize(450, 150)
        self.gLayout = QGridLayout(self)
        self.pBulunan = QPushButton(self)
        self.pBulunan.setEnabled(False)
        self.pBulunan.clicked.connect(self.bulunan)
        self.gLayout.addWidget(self.pBulunan, 3, 2, 1, 1)
        self.mesaj = QLabel(self)
        self.gLayout.addWidget(self.mesaj, 0, 0, 1, 3)
        self.pBar = QProgressBar(self)
        self.pBar.setProperty("value", 0)
        self.gLayout.addWidget(self.pBar, 1, 0, 1, 3)
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gLayout.addItem(spacerItem, 3, 0, 1, 1)
        spacerItem1 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.gLayout.addItem(spacerItem1, 2, 0, 1, 3)

        self.setWindowTitle(u"Sistemi taramaya karar verdim...")
        self.pBulunan.setText(u"Bulunan Virüsleri Sil")
        self.mesaj.setText(u"")
        self.mesaj.setMaximumWidth(430)

        self.progress = QBasicTimer()
        self.progress.start(1000, self)
        self.sayac = 0
        self.mesaj.setText(u"Dosya bilgileri alınıyor...")


    def timerEvent(self, event):
        import time
        from PyQt4.QtGui import QApplication
        self.dosyaListesi = list()
        if sys.platform == "linux2":
            dosyalar = os.walk("/home")
        if sys.platform == "win32":
            dosyalar = os.walk("C:\\")
        for i in dosyalar:
            for k in i[-1]:
                QApplication.processEvents()
                self.dosyaListesi.append(os.path.join(i[0],k))

        self.dosyaSayisi = len(self.dosyaListesi)
        self.pBar.setMaximum(self.dosyaSayisi)
        while len(self.dosyaListesi)>self.sayac:
            self.mesaj.setText(self.dosyaListesi[self.sayac])
            self.sayac += 1
            self.pBar.setValue(self.sayac)
            time.sleep(0.001)
            QApplication.processEvents()

        self.pBulunan.setEnabled(True)
        self.mesaj.setText(u"Sayamayacağım kadar çok virüs bulundu...")
        self.progress.stop()

    def bulunan(self):
        QMessageBox.information(self, u"Sildim gitti!", u"Sayamayacağım kadar virüs silindi!", u"Bileğine Kuvvet!")
        self.close()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            pass

    def closeEvent(self, event):
        event.ignore()
        self.hide()