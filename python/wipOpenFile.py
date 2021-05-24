############win $$$$$$$SOME PICE OF SCRIPTS USEFULL IN THE FUTURE###########

import webbrowser, os
path="Y:/Unidades compartidas/Quaker/SEQUENCES/STAIRCASE/Production/07_To_Client/WIPS/Interno/210521/Fran/"
webbrowser.open(os.path.realpath(path))


#################win #####
import os

path = nuke.selectedNode()['file'].value()
path = os.path.realpath(path)
os.startfile(path)
#########################
print nuke.selectedNode()['label'].value()

print tcl[value]
return nuke.selectedNode()['label'].value()
