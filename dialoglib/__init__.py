#-*- coding:utf-8 -*-

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

import os

dizin_listesi = os.listdir(os.path.abspath(os.path.dirname(__file__)))

def dialogList(list):
    for py in list:
        if not py.startswith("__init__"):
            if py[-3:] != "pyc" and py[:-3] == ".py":
                yield py[:-3]

kod = ""
for i in dialogList(dizin_listesi):
    kod += "import %s\n"%i

kod += "\n\n"
kod += "all = ["

for i in dialogList(dizin_listesi):
    kod += "%s.DMessage, "%i

kod += "]\n"

exec(kod)

