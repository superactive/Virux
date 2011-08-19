
import os

dizin_listesi = os.listdir(os.path.abspath(os.path.dirname(__file__)))

def dialogList(list):
    for py in list:
        if not py.startswith("__init__"):
            if py[-3:] != "pyc":
                yield py[:-3]

kod = ""
for i in dialogList(dizin_listesi):
    kod += "import %s\n"%i

kod += "\n\n"
kod += "all = ["

for i in dialogList(dizin_listesi):
    kod += "%s.DMessage, "%i

kod += "]\n"

print kod
exec(kod)

