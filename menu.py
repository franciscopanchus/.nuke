#---------------------------------------------------------	
#menu.py
#Version 1.0.0
#Last Update 30/04/20
#---------------------------------------------------------

import nuke
import platform 

Win_dir = 'C:\Users\Franc\.nuke'
MacOSX = ''
Linux_Dir = '/home/franc/.nuke'

#Set Global directory
if platform.system() == "Windows":
	dir = Win_dir
elif platform.system() == "Darwin":
	dir = MacOSX_dir
elif platform.system() == "Linux":
	dir = Linux_Dir
else:
	dir = None


