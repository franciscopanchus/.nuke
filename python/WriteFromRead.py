
#(start)
#---------------------------------------------------------
#WriteFromRead.py
#Version 1.0.0
#Last Update 21/10/20
#Francisco Biancardi
#basic Form, tif to exr
#---------------------------------------------------------
import nuke
import os

def readFromWrite():
    
    s = nuke.selectedNodes()   
    
    for x in s:
        if x.Class() == "Read":

            w = nuke.createNode('Write', inpanel=False)
            w.setInput(0,x)
            newname = x["file"].value().replace('tif', 'exr')
            w["file"].setValue(newname)
            w["channels"].setValue("rgba")
            w["file_type"].setValue(3)
        else:
            print "{}it´s not a read".format(x.knobname)

#---------------------------------------------------------
#(end)


readFromWrite()
