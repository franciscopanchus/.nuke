#---------------------------------------------------------	
#menu.py
#Version 1.0.1
#Last Update 02/05/20
#---------------------------------------------------------


#---------------------------------------------------------
#GLOBAL PATHS:::::::::::::::::::::::::::::::::::::::::::::
#---------------------------------------------------------

nuke.pluginAddPath('./icons')
nuke.pluginAddPath('./gizmos/bm_NukeTools')


#---------------------------------------------------------
#GLOBAL IMPORTS:::::::::::::::::::::::::::::::::::::::::::
#---------------------------------------------------------



import nuke
import platform 
import nukescripts

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


#---------------------------------------------------------
#GLOBAL DEFAULTS::::::::::::::::::::::::::::::::::::::::::
#---------------------------------------------------------

nuke.knobDefault('shutteroffset', "centered")
nuke.knobDefault('Tracker4.shutteroffset', "centered")
nuke.knobDefault('Tracker4.label', "Motion: [value transform]\nRef Frame: [value reference_frame]")



nuke.addOnUserCreate(lambda:nuke.thisNode()
['reference_frame'].setValue(nuke.frame()), nodeClass='Tracker4')

nuke.addOnUserCreate(lambda:nuke.thisNode()
['first_frame'].setValue(nuke.frame()), nodeClass='FrameHold')

#---------------------------------------------------------
#COSTUME MENU:::::::::::::::::::::::::::::::::::::::::::::
#---------------------------------------------------------

utilitiesMenu = nuke.menu('Nuke').addMenu('Utilities')

utilitiesMenu.addCommand('Autocrop', 'nukescripts.autocrop()')

#---------------------------------------------------------
#TOOLS MENU:::::::::::::::::::::::::::::::::::::::::::::::
#---------------------------------------------------------


myGizmosMenu = nuke.menu('Nodes').addMenu('myGizmosMenu', icon="myGizmos_icon.png")
myGizmosMenu.addCommand('bm_CameraShake', "nuke.createNode('bm_CameraShake')", icon="bm_CameraShake_icon.png")
myGizmosMenu.addCommand('bm_CurveRemapper', "nuke.createNode('bm_CurveRemapper')", icon="bm_CurveRemapper_icon.png")
myGizmosMenu.addCommand('bm_EdgeMatte', "nuke.createNode('bm_EdgeMatte')", icon="bm_EdgeMatte_icon.png")
myGizmosMenu.addCommand('bm_Lightwrap', "nuke.createNode('bm_Lightwrap')", icon="bm_Lightwrap_icon.png")
myGizmosMenu.addCommand('bm_MatteCheck', "nuke.createNode('bm_MatteCheck')", icon="bm_MatteCheck_icon.png")
myGizmosMenu.addCommand('bm_NoiseGen', "nuke.createNode('bm_NoiseGen')", icon="bm_NoiseGen.png")
myGizmosMenu.addCommand('bm_OpticalGlow', "nuke.createNode('bm_OpticalGlow')", icon="bm_OpticalGlow_icon.png")

#---------------------------------------------------------
#KeyBoard ShortCuts:::::::::::::::::::::::::::::::::::::::
#---------------------------------------------------------

nuke.menu('Nodes').addCommand("Transform/Tracker", "nuke.createNode('Tracker4')", "ctrl+t", icon="Tracker.png", shortcutContext=2)

