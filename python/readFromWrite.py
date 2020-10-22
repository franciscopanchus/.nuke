#---------------------------------------------------------
#readFromWrite.py
#Version 1.0.0
#Last Update 21/10/20
#Francisco Biancardi
#basic Form, tif to exr
#---------------------------------------------------------------------------------------------------------

import nuke
import os

def readFromWrite():
    
    s = nuke.selectedNodes()
    w = nuke.createNode('Write', inpanel=False)
    
    for x in s:
        newname = x["file"].value().replace('tif', 'exr')
        w["file"].setValue(newname)
        w["channels"].setValue("rgba")
        w["file_type"].setValue(3)



readFromWrite()
