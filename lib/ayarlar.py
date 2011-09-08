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

from PyQt4.QtGui import QDialog, QPushButton, QGridLayout, QLabel, QSpacerItem, QSizePolicy, QTreeWidget, QTreeWidgetItem, QIcon,\
QPixmap, QGroupBox, QDialogButtonBox, QWidget
from PyQt4.QtCore import Qt, QSettings
import os, sys
from dialoglib import __all__ as DOptions

class DAyarlar(QDialog):
    def __init__(self, parent):
        QDialog.__init__(self, parent)
        self.resize(600, 375)
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.treeWidget = QTreeWidget(self)
        self.treeWidget.setMaximumSize(200, 1500)

        self.virux = QTreeWidgetItem(self.treeWidget)
        self.virux.setExpanded(True)
        icon = QIcon()
        icon.addPixmap(QPixmap("data/logo.png"), QIcon.Normal, QIcon.On)
        self.virux.setIcon(0, icon)
        item_1 = QTreeWidgetItem(self.virux)
        item_1 = QTreeWidgetItem(self.virux)
        self.dialog = QTreeWidgetItem(self.treeWidget)
        self.dialog.setExpanded(True)
        item_1 = QTreeWidgetItem(self.dialog)
        item_1 = QTreeWidgetItem(self.dialog)
        self.treeWidget.header().setVisible(False)

        self.gridLayout.addWidget(self.treeWidget, 0, 0, 1, 1)
        self.groupBox = QGroupBox(self)
        self.groupBox.setFlat(True)

        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setSpacing(0)
        self.widget = QWidget(self.groupBox)
        self.gridLayout_4 = QGridLayout(self.widget)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setMargin(0)
        spacerItem = QSpacerItem(300, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 1, 1, 1)
        self.pButton = QPushButton(self)
        self.pButton.setText("asd")
        self.pButton.setDefault(True)
        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.addButton(self.pButton, QDialogButtonBox.AcceptRole)
        #self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 2)


        self.setWindowTitle("Virux Ayarlar")
        self.treeWidget.headerItem().setText(0, "")
        self.treeWidget.topLevelItem(0).setText(0, u"Virux")
        self.treeWidget.topLevelItem(0).child(0).setText(0, u"Virux1")
        self.treeWidget.topLevelItem(0).child(1).setText(0, u"Virux2")
        self.treeWidget.topLevelItem(1).setText(0, u"Dialog")
        self.treeWidget.topLevelItem(1).child(0).setText(0, u"Dialog1")
        self.treeWidget.topLevelItem(1).child(1).setText(0, u"Dialog2")
        self.groupBox.setTitle(u"GroupBox")
        self.groupYaz()

        self.treeWidget.itemPressed.connect(self.lale)

    def lale(self, item):
        print item
        self.groupBox.setTitle(item.text(0))

    def groupYaz(self):
        for option in DOptions:
            if hasattr(option, "getOption"):
                #self.gridLayout_3.addWidget(option.getOption(), 0, 0, 1, 1)
                item = QTreeWidgetItem(self.dialog)
                a = option.getOption()
                if hasattr(a, "name"):
                    item.setText(0, a.name)
                else:
                    item.setText(0, "Fuck")

        #self.gridLayout_3.addWidget(a, 0, 0, 1, 1)