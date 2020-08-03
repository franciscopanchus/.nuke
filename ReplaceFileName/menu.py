#---------------------------------------------------------
#menu.py
#Version 1.0.0
#Last Update 20/07/20
#Francisco Biancardi
#---------------------------------------------------------
import nuke
import ReplaceFileName

nuke.menu("Nuke").findItem("Utilities")
utilitiesMenu.addCommand('Replace File Namessssssss', 'ReplaceFileName.replaceFileName()')