# ---------------------------------------------------------
# colorNode.py
# Version 1.0.1
# Last Update 01/11/20
# Francisco Biancardi
# simple, pick nodes and colored them
# ---------------------------------------------------------


def colorNodo():
    chooseColor = nuke.getColor()
    nodes = nuke.selectedNodes()
    info = []

    for node in nodes:
        if nodes == False:
            pass
        else:
            node.knob("tile_color").setValue(chooseColor)


colorNodo()
