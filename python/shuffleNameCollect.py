# (start)
# ---------------------------------------------------------
# shuffleNameCollect.py
# Version 1.0.0
# Last Update 31/10/20
# Francisco Biancardi
# selected shuffles and add names to a stickynote
# ---------------------------------------------------------
import nuke
import os.path 

def shuffleNameCollect():
    nodes = nuke.selectedNodes()
    info = []

    if nodes == []:
        pass

    elif nodes != []:
        for node in nodes:
            if node.Class() == "Shuffle1" or node.Class() == "Shuffle":
                info.append(node.knob("in").value()) 

        if info != []:
            node = nuke.selectedNode()
            path = node.metadata('input/filename')           
            spliteado = (os.path.splitext(os.path.basename(path))[0]).split("_")
            killframes = spliteado.pop()
            newfilename = ("_").join(spliteado)

            sticky = nuke.nodes.StickyNote(label= newfilename +'\n'+ (', ''\n'.join(info)), note_font_size=80,)
            nuke.show(sticky)
            nuke.zoom(0.5, [sticky.xpos(), sticky.ypos()])

        else:
             nuke.message("please select a shuffle node")


shuffleNameCollect()



# ---------------------------------------------------------
# (end)


shuffleNameCollect()
