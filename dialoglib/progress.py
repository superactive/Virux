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

from PyQt4.QtGui import QPushButton, QGridLayout, QLabel, QProgressBar, QSpacerItem, QSizePolicy, QMessageBox, QWidget, QSpinBox
from PyQt4.QtCore import QThread, SIGNAL, QString
from basedialog import VDialog
import os, sys, random

class Thread(QThread):
    def __init__(self, parent):
        QThread.__init__(self, parent)
        self.parent = parent
        self.sayac = 0

    def run(self):
        self.dosyaListesi = list()
        dizin = random.choice(["/home","/usr", "/dev", "/etc", "/var", "/lib"])
        if sys.platform == "linux2":
            dosyalar = os.walk(dizin)
        if sys.platform == "win32":
            dosyalar = os.walk("C:\\")
        for i in dosyalar:
            for k in i[-1]:
                self.dosyaListesi.append(os.path.join(i[0],k))

        self.dosyaSayisi = len(self.dosyaListesi)
        self.parent.pBar.setMaximum(self.dosyaSayisi)
        while len(self.dosyaListesi)>self.sayac:
            self.parent.mesaj.setText(QString.fromUtf8(self.dosyaListesi[self.sayac]))
            self.sayac += 1
            self.emit(SIGNAL("setValue"), self.sayac)
            self.msleep(1)

        self.parent.pBulunan.setEnabled(True)
        self.parent.mesaj.setText(u"Sayamayacağım kadar çok virüs bulundu...")

class Option(QWidget):
   
    def __init__(self):
        QWidget.__init__(self)
        self.resize(168, 86)
        self.name = "Progress"
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setMargin(0)
        self.label_2 = QLabel(self)
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.spinBox = QSpinBox(self)
        self.spinBox.setMinimum(60)
        self.spinBox.setMaximum(600)
        self.gridLayout.addWidget(self.spinBox, 0, 2, 1, 1)
        self.spinBox_2 = QSpinBox(self)
        self.spinBox_2.setMinimum(120)
        self.spinBox_2.setMaximum(600)
        self.spinBox_2.setProperty("value", 600)
        self.gridLayout.addWidget(self.spinBox_2, 1, 2, 1, 1)
        self.label = QLabel(self)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2.setText(u"Max Süre(dk):")
        self.label.setText(u"Min. Süre(dk):")


class DMessage(VDialog):
    def __init__(self, parent):
        VDialog.__init__(self, parent)
        self.resize(450, 150)
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

        self.progress = Thread(self)
        self.progress.start()

        self.connect(self.progress, SIGNAL("setValue"), self.pBar.setValue)

        self.mesaj.setText(u"Dosya bilgileri alınıyor...")

    def bulunan(self):
        QMessageBox.information(self, u"Sildim gitti!", u"Sayamayacağım kadar virüs silindi!", u"Bileğine Kuvvet!")
        self.close()

    @staticmethod
    def getOption():
        return Option()