# (start)
# ---------------------------------------------------------
# shuffleNameCollect.py
# Version 1.0.0
# Last Update 31/10/20
# Francisco Biancardi
# selected shuffles and add names to a stickynote
# ---------------------------------------------------------
import nuke


def shuffleNameCollect():
    nodes = nuke.selectedNodes()
    info = []

    if nodes == []:
        pass

    else:
        for node in nodes:
            if node.Class() == "Shuffle1" or node.Class() == "Shuffle":
                info.append(node.knob("in").value())

            else:
                nuke.message("please select a shuffle node")

        if info == 0 or nodes == 0:
            exit()
        else:
            sticky = nuke.nodes.StickyNote(label=(', ''\n'.join(info)), note_font_size=130)
            node = nuke.selectedNode()
            nuke.zoom(0.5, [sticky.xpos(), sticky.ypos()])



# ---------------------------------------------------------
# (end)


shuffleNameCollect()
