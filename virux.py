#!/usr/bin/python
#-*- coding:utf-8 -*-
import sys, os.path, random
from PyQt4.QtGui import QMenu, QSystemTrayIcon, QAction, QIcon, QWidget, QApplication
from PyQt4.QtCore import QBasicTimer
from dialoglib import all

class SystemTray(QSystemTrayIcon):
    def __init__(self, parent=None):
        QSystemTrayIcon.__init__(self, parent)
        self.parent = parent
        self.menu = QMenu()

        self.aKoru = QAction(self.menu)
        self.aKoru.setText("Koru")
        self.aKoru.setCheckable(True)
        self.aKoru.setChecked(True)
        self.aKoru.triggered.connect(self.koru)
        self.menu.addAction(self.aKoru)

#        self.aKapat = QAction(self.menu)
#        self.aKapat.setText("Kapat")
#        self.aKapat.triggered.connect(self.close)
#        self.menu.addAction(self.aKapat)

        self.setIcon(QIcon(os.path.join("data","logo.png")))
        self.setContextMenu(self.menu)

        self.activated.connect(self.mesaj)

        self.timer = QBasicTimer()
        self.sayac = 0

        self.timer.start(200, self)

        self.bocuk = [i for i in os.listdir(os.path.join("data","bocuk"))]
        self.bocuk.sort()

        self.dialogList = all

        self.timer2 = QBasicTimer()
        self.timer2.start(random.randrange(1000*10000,1000*50000), self)

    def timerEvent(self, event):
        if event.timerId() == self.timer.timerId():
            if self.sayac < 10:
                self.setIcon(QIcon(os.path.join("data","bocuk",self.bocuk[self.sayac])))
                self.sayac += 1
            else:
                self.sayac = 0
        if self.aKoru.isChecked():
            if event.timerId() == self.timer2.timerId():
                dialog = random.choice(self.dialogList)
                dialog = dialog(self.parent)
                dialog.show()
                self.timer2.start(random.randrange(1000*10000,1000*50000), self)
        
            
    def mesaj(self, reason):
        if reason == self.Trigger:
            self.showMessage("Virux", u"GNU/Linux için antivirüs uygulaması", self.NoIcon, 10000)

        if reason == self.MiddleClick:
            dialog = random.choice(self.dialogList)
            dialog = dialog(self.parent)
            dialog.show()

    def koru(self):
        if not self.aKoru.isChecked():
            self.timer.stop()
            self.setIcon(QIcon(os.path.join("data","logo.png")))

        else:
            self.timer.start(200, self)
        

class HideWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowIcon(QIcon(os.path.join("data","logo.png")))
        self.systemTray = SystemTray(self)
        self.systemTray.show()

    def closeEvent(self, event):
        event.ignore()
        self.hide()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Virux")
    app.setApplicationVersion("0.2")

    gui = HideWidget()
    #gui.show()

    sys.exit(app.exec_())