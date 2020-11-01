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

    elif nodes != []:
        for node in nodes:
            if node.Class() == "Shuffle1" or node.Class() == "Shuffle":
                info.append(node.knob("in").value()) 

        #if info == 0 and nodes == 0:
        #    exit()
        if info != []:
            sticky = nuke.nodes.StickyNote(label=(', ''\n'.join(info)), note_font_size=70,)
            nuke.show(sticky)
            nuke.zoom(0.5, [sticky.xpos(), sticky.ypos()])

        else:
             nuke.message("please select a shuffle node")



# ---------------------------------------------------------
# (end)


shuffleNameCollect()
