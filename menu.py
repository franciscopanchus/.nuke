#---------------------------------------------------------	
#menu.py
#Version 1.0.2
#Last Update 03/05/20
#---------------------------------------------------------


#---------------------------------------------------------
#GLOBAL PATHS:::::::::::::::::::::::::::::::::::::::::::::
#---------------------------------------------------------

''''''
nuke.pluginAddPath('./gizmos/bm_NukeTools')
nuke.pluginAddPath('./gizmos/Nukepedia/VoxelSystem')

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
nuke.knobDefault('Merge2.bbox',"B")

#----------------CAMERA DEFAULTS-------------------------
camproject = nuke.menu('Nodes').findItem("3D")
camproject.addCommand('Camera',"nuke.createNode('camera_project_1.0.0.nk')")

#----------------TRACKER DEFAULTS-------------------------
#nuke.knobDefault('Tracker4.shutteroffset', "centered")
#nuke.knobDefault('Tracker4.label', "Motion: [value transform]\nRef Frame: [value reference_frame]")
#nuke.addOnUserCreate(lambda:nuke.thisNode()
#['reference_frame'].setValue(nuke.frame()), nodeClass='Tracker4')


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
myGizmosMenu.addCommand('Remove_advanced_v1', "nuke.createNode('Remove_advanced_v1')", icon="NodeDisable_icon.png")

nukepedia = nuke.menu('Nodes').addMenu('nukepedia', icon="Nukepedia.png")
nukepedia.addCommand('V_Shape', "nuke.createNode('V_Shape')")

ElMago = nuke.menu('Nodes').addMenu('ElMago', icon="jfbTool_icon.png")
ElMago.addCommand('Image Plane', "imageplane.imagePlane()", icon="imageplane_icon.png")
ElMago.addCommand('NodeDisable', "nuke.createNode('NodeDisable')", icon="NodeDisable_icon.png")
ElMago.addCommand('KillOutline', "nuke.createNode('KillOutline')", icon="killOutline.png")

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
#........................python 101
import W_hotbox, W_hotboxManager
import hubCamera
import shuffleShortCut
import listNavigator
import filepathLister
#import pastedSelected #check it, it is working wrong
import NodeLabelpop
import NodeXtimes
import moblur_controller
import shortCutOperationSwicher
import shortcut_NodeCustumizer
import imageplane
import deleteDisablenode
import renamingFiles
import layersToShuffles
#.................-Dev. python tools
import renderFinished
import readWrite #create a read from the write node
import autoSave
#import cryptomatte_utilities


#---------------------------------------------------------
#COSTUME MENU:::::::::::::::::::::::::::::::::::::::::::::
#---------------------------------------------------------


#------------Custom Menu and assignment-------------------

utilitiesMenu = nuke.menu('Nuke').addMenu('Utilities')
utilitiesMenu.addCommand('Autocrop', 'nukescripts.autocrop()')
utilitiesMenu.addCommand('filepathLister', 'filepathLister.file_lister()')
utilitiesMenu.addCommand('Delete disable Node', 'deleteDisablenode.deleteDisable()')
utilitiesMenu.addCommand('Rename File sequence', 'renamingFiles.renameFile()')
utilitiesMenu.addCommand('Create Read from Write', 'readWrite.readWrite()', "ctrl+r")
utilitiesMenu.addCommand("AutoBackUp/open backup directory", "autoSave.open_backup_dir()")
utilitiesMenu.addCommand("Layers to Shuffles", "layersToShuffles.layersToShuffles()")
nuke.addOnScriptSave(autoSave.make_backup)

HubMenu = nuke.menu('Nuke').addMenu('HubMenu')
HubMenu.addCommand('hubCamera', 'hubCamera.HubCamera()')

#cryptomatte_utilities.setup_cryptomatte_ui()

#---------After Render Sound and Message

nuke.addAfterRender(renderFinished.notify_user)

''''''