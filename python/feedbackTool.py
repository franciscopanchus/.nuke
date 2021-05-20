#---------------------------------------------------------
#feedbackTool.py
#Version 1.0.2
#Last Update 19/05/21
#Francisco Biancardi
#---------------------------------------------------------
import nuke
import os

def loadFeedback():

    scriptDirectory = nuke.script_directory()
    cutDirectory = scriptDirectory.split('/')
    eliminateVariable = []
    readList = []
    allread = nuke.allNodes('Read')

#---------------------------getting the filepath---------------------------
    for x in cutDirectory:
        if x == '03 NK':
            del x
        else:
            eliminateVariable.append(x)

    feedbackDirectory = '/'.join(eliminateVariable) + "/05 Other files/feedback/"

#---------------------------watch your reads my friend---------------------------
    for f in allread:
        readList.append(f.knob('label').getValue())

#---------------------------creating or not the read---------------------------
    for x in os.listdir(feedbackDirectory):
        if x in readList:
            print "allready exist here"
        else:
            feedback = nuke.createNode('Read', inpanel=False)
            feedback['file'].setValue(feedbackDirectory + x)
            feedback['label'].setValue(x)
