#---------------------------------------------------------	
#menu.py
#Version 1.0.2
#Last Update 03/05/20
#---------------------------------------------------------


#---------------------------------------------------------
#GLOBAL PATHS:::::::::::::::::::::::::::::::::::::::::::::
#---------------------------------------------------------


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

#----------------TRACKER DEFAULTS-------------------------
nuke.knobDefault('Tracker4.shutteroffset', "centered")
nuke.knobDefault('Tracker4.label', "Motion: [value transform]\nRef Frame: [value reference_frame]")
nuke.addOnUserCreate(lambda:nuke.thisNode()
['reference_frame'].setValue(nuke.frame()), nodeClass='Tracker4')


#----------------FRAMEHOLD DEFAULTS-----------------------
nuke.addOnUserCreate(lambda:nuke.thisNode()
['first_frame'].setValue(nuke.frame()), nodeClass='FrameHold')


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
myGizmosMenu.addCommand('NodeDisable', "nuke.createNode('NodeDisable')", icon="NodeDisable_icon.png")
myGizmosMenu.addCommand('Remove_advanced_v1', "nuke.createNode('Remove_advanced_v1')", icon="NodeDisable_icon.png")



#---------------------------------------------------------
#KeyBoard ShortCuts:::::::::::::::::::::::::::::::::::::::
#---------------------------------------------------------

nuke.menu('Nodes').addCommand("Transform/Tracker", "nuke.createNode('Tracker4')", "ctrl+t", icon="Tracker.png", shortcutContext=2)

#------------Merge Node Shortcut-------------------------
mergeMenu = nuke.menu('Nodes').findItem("Merge/Merges")

mergeMenu.addCommand('Stencil', 'nuke.createNode("Merge2", "operation stencil bbox B")', "alt+o", icon= "SplitAndJoin.png", shortcutContext=2)
mergeMenu.addCommand('Mask', 'nuke.createNode("Merge2", "operation mask bbox B")', "alt+m", icon= "SplitAndJoin.png", shortcutContext=2)
mergeMenu.addCommand('Plus', 'nuke.createNode("Merge2", "operation plus bbox B")', "alt+p", icon= "MergePlus.png", shortcutContext=2)
mergeMenu.addCommand('From', 'nuke.createNode("Merge2", "operation from bbox B")', "alt+f", icon= "DifferenceKeyer.png", shortcutContext=2)

#------------Paste for multiples nodes--------------------

editPaste = nuke.menu('Nuke').findItem("Edit")
#editPaste.addCommand('Paste','pastedSelected.pastedSelected()', "ctrl+g", shortcutContext=2)


#---------------------------------------------------------
#PYTHON SCRIPTS:::::::::::::::::::::::::::::::::::::::::::
#---------------------------------------------------------

import W_hotbox, W_hotboxManager
import hubCamera
import shuffleShortCut
import listNavigator
import filepathLister
#import pastedSelected
import NodeLabelpop
import NodeXtimes
import moblur_controller
import shortCutOperationSwicher
import shortcut_NodeCustumizer

#---------------------------------------------------------
#COSTUME MENU:::::::::::::::::::::::::::::::::::::::::::::
#---------------------------------------------------------


#------------Custom Menu and assignment-------------------

utilitiesMenu = nuke.menu('Nuke').addMenu('Utilities')
utilitiesMenu.addCommand('Autocrop', 'nukescripts.autocrop()')
utilitiesMenu.addCommand('filepathLister', 'filepathLister.file_lister()')



HubMenu = nuke.menu('Nuke').addMenu('HubMenu')
HubMenu.addCommand('hubCamera', 'hubCamera.HubCamera()')



