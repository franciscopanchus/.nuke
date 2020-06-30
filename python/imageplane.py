#---------------------------------------------------------
#imageplane_1.0.0.py
#Version 1.0.0
#Last Update 28/06/20
#Francisco Biancardi
#---------------------------------------------------------
import nuke
import hubCamera

################PICK CAMERA####################
def imagePlane():

    g = nuke.createNode('Group')

    # ------creating knobs outside---------#

    projectionframe = nuke.Array_Knob("projectionframe", "projection frame")
    zposition = nuke.Array_Knob("zposition", "zposition")
    pickcamera = nuke.PyScript_Knob("pickcamera", "Pick Camera", "imageplane.PickCamera()")

    g.addKnob(projectionframe)
    g.addKnob(zposition)
    g.addKnob(pickcamera)

    #:::::::::::::::GROUP BEGININ:::::::::::::::
    g.begin()

    n = nuke.createNode('camera_project_1.0.0.nk')
    #hubCamera.HubCamera()
    p = nuke.selectedNode()
    k = p.knob("create_projection")
    k.execute()

    searchcamera = nuke.allNodes()
    camera = []
    for x in searchcamera:
        if x.Class() == "Camera2":
            camera.append(x)
            x["projection_frame"].setExpression("parent.projectionframe")
            x["zposition"].setExpression("parent.zposition")


    g.end()
    #:::::::::::::::GROUP END:::::::::::::::


def PickCamera():
    ################PICK CAMERA script ####################

    outgroup = nuke.thisNode()
    outgroup.end()
    selectedCamera = nuke.selectedNode()  # the other camera, the source

    if selectedCamera.Class() == 'Camera2':

        #:::::::::::::::GROUP BEGININ:::::::::::::::
        outgroup.begin()

        searchcamera = nuke.allNodes()

        for x in searchcamera:
            if x.Class() == "Camera2":
                x.readKnobs(selectedCamera.writeKnobs())

        outgroup.end()
        #:::::::::::::::::GROUP END:::::::::::::::::

