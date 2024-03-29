#!/usr/bin/env python
#-*- coding:utf-8 -*-

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

import sys, os, random, icon_rc
from PyQt4.QtGui import QMenu, QSystemTrayIcon, QAction, QIcon, QWidget, QApplication
from PyQt4.QtCore import QBasicTimer, QSettings, QDir, QSharedMemory
from dialoglib import __all__
from lib import DHakkinda, DAyarlar

mainPath = os.path.abspath(os.path.dirname(__file__))

class SystemTray(QSystemTrayIcon):
    def __init__(self, parent=None):
        QSystemTrayIcon.__init__(self, parent)
        self.parent = parent
        self.menu = QMenu()

        self.aAyarlar = QAction(self.menu)
        self.aAyarlar.setText(u"Ayarlar")
        self.aAyarlar.triggered.connect(self.ayarlar)
        self.menu.addAction(self.aAyarlar)

        self.menu.addSeparator()

        self.aKoru = QAction(self.menu)
        self.aKoru.setText(u"Koru")
        self.aKoru.setCheckable(True)
        self.aKoru.setChecked(setting.value("ContextMenu/Koru").toBool())
        self.aKoru.triggered.connect(self.koru)
        self.menu.addAction(self.aKoru)

        self.aBaslat = QAction(self.menu)
        self.aBaslat.setText(u"Açılışta Başlat")
        self.aBaslat.setCheckable(True)
        self.aBaslat.setChecked(setting.value("ContextMenu/AcilistaBaslat").toBool())
        self.aBaslat.triggered.connect(self.baslat)
        self.menu.addAction(self.aBaslat)

        self.menu.addSeparator()

        self.aHakkinda = QAction(self.menu)
        self.aHakkinda.setText(u"Virux Hakkında")
        self.aHakkinda.triggered.connect(self.hakkinda)
        self.menu.addAction(self.aHakkinda)

        self.aKapat = QAction(self.menu)
        self.aKapat.setText(u"Kapat")
        self.aKapat.triggered.connect(self.close)
        self.menu.addAction(self.aKapat)

        self.setIcon(QIcon(":logo.png"))
        self.setContextMenu(self.menu)

        self.activated.connect(self.mesaj)

        self.timer = QBasicTimer()
        self.sayac = 0

        self.timer.start(200, self)
        self.koru()

        self.dialogList = __all__
        self.timer2 = QBasicTimer()
        self.timer2.start(random.randrange(setting.value("DialogOpen/MinimumSure").toInt()[0],
                                           setting.value("DialogOpen/MaksimumSure").toInt()[0]), self)

    def close(self):
        sys.exit()

    def hakkinda(self):
        hakkinda = DHakkinda(self.parent)
        hakkinda.show()

    def ayarlar(self):
        ayarlar = DAyarlar(self.parent)
        ayarlar.show()

    def timerEvent(self, event):
        if event.timerId() == self.timer.timerId():
            if self.sayac < 10:
                self.setIcon(QIcon(":/bocuk/data/bocuk/%s.png"%str(self.sayac).zfill(2)))
                self.sayac += 1
            else:
                self.sayac = 0
        if self.aKoru.isChecked():
            if event.timerId() == self.timer2.timerId():
                dialog = random.choice(self.dialogList)
                dialog = dialog(self.parent)
                dialog.show()
                self.timer2.start(random.randrange(setting.value("DialogOpen/MinimumSure").toInt(),
                                                   setting.value("DialogOpen/MaksimumSure").toInt()), self)

    def baslat(self):
        if sys.platform == "win32":
            self.windows()
        else:
            self.linux()


    def windows(self):
        import _winreg
        if self.aBaslat.isChecked():
            setting.setValue("ContextMenu/AcilistaBaslat", True)
            setting.sync()
            regPath = "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run"
            self.reg = _winreg.OpenKeyEx(_winreg.HKEY_LOCAL_MACHINE, regPath, 0, _winreg.KEY_ALL_ACCESS)
            _winreg.SetValueEx(self.reg, "Virux", 0, _winreg.REG_SZ, os.path.join(mainPath,__file__))
        else:
            setting.setValue("ContextMenu/AcilistaBaslat", False)
            setting.sync()
            _winreg.DeleteValue(self.reg, "Virux")
        #_winreg.CloseKey(self.reg)

    def linux(self):
        if not self.aBaslat.isChecked():
            setting.setValue("ContextMenu/AcilistaBaslat", False)
            dosyaYolu = os.path.join(str(QDir.homePath()),".kde","Autostart", "Virux.desktop")
            if os.path.isfile(dosyaYolu):
                os.remove(dosyaYolu)
        else:
            setting.setValue("ContextMenu/AcilistaBaslat", True)
            dosyaYolu = os.path.join(str(QDir.homePath()),".kde","Autostart", "Virux.desktop")
            desktop = """[Desktop Entry]
            Comment[tr]=Platform bağımsız bir antivirüs uygulaması
            Comment=Platform bağımsız bir antivirüs uygulaması
            Exec=python %s/virux.py
            GenericName[tr]=Platform bağımsız bir antivirüs uygulaması
            GenericName=Platform bağımsız bir antivirüs uygulaması
            Icon=%s
            Type=Application
            Name[tr]=Virux
            Name=Virux
            Path=
            StartupNotify=true
            Terminal=false
            """%(mainPath, os.path.join(mainPath, "data", "logo.png"))
            yaz = open(dosyaYolu, "w")
            yaz.write(desktop)
            yaz.close()

            
    def mesaj(self, reason):
        if reason == self.Trigger:
            self.showMessage("Virux", u"Eğlence amaçlı antivirüs uygulaması :P", self.NoIcon, 10000)

        if reason == self.MiddleClick:
            dialog = random.choice(self.dialogList)
            dialog = dialog(self.parent)
            dialog.show()

    def koru(self):
        if not self.aKoru.isChecked():
            self.timer.stop()
            self.setIcon(QIcon(":/logo/data/logo.png"))
            setting.setValue("ContextMenu/Koru", False)
        else:
            self.timer.start(200, self)
            setting.setValue("ContextMenu/Koru", True)
        

class HideWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowIcon(QIcon(":/logo/data/logo.png"))
        self.systemTray = SystemTray(self)
        self.systemTray.show()

    def closeEvent(self, event):
        event.ignore()
        self.hide()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    app.setApplicationName("Virux")
    app.setApplicationVersion("0.5")

    sharedMemory = QSharedMemory("f33a4b06-72f5-4b72-90f4-90d606cdf98c")
    if sharedMemory.create(512, QSharedMemory.ReadWrite) == False:
        sys.exit()
        
    if sys.platform == "win32":
        setting = QSettings("Virux.conf", QSettings.IniFormat)
    else:
        setting = QSettings("Virux", "Virux")
    if not os.path.isfile(setting.fileName()):
        setting.setValue("ContextMenu/AcilistaBaslat", False)
        setting.setValue("ContextMenu/Koru", True)
        setting.setValue("DialogOpen/MinimumSure", 1000*7200)
        setting.setValue("DialogOpen/MaksimumSure", 1000*36000)

    gui = HideWidget()
    #gui.show()

    sys.exit(app.exec_())
