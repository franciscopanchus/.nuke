#---------------------------------------------------------
#deleteDisablenode.py
#Version 1.0.0
#Last Update 30/06/20
#Francisco Biancardi
#---------------------------------------------------------


import nuke

def deleteDisable():
    question = nuke.ask("Do you want to deleted all disabled nodes?")
    allnodes = nuke.allNodes()

    if question == True:
        for node in allnodes:
            if node.Class() == "Viewer":
                print "there is a viewer here"

            elif node['disable'].value() == True:
                nuke.delete(node)
            else:
                print "{} it is enable".format(node['name'].value())

    elif question == False:
        nuke.message("you are a chicken")
