#---------------------------------------------------------
#ImagePlane.py
#Version 1.0.0
#Last Update 19/06/20
#Author: Francisco Biancardi
# -------------------------------------------------------

import nuke

def imagePlane():

    selectedNode = nuke.selectedNode()
    node_camera = "Camera2"

    if selectedNode.Class() == node_camera:
        print "hola si lo es"

    else:
        print "no lo es"


    
