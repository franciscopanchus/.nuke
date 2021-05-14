#---------------------------------------------------------
#AutoWritefran.py
#Version 1.0.1
#Last Update 14/05/21
#Francisco Biancardi
#---------------------------------------------------------
#------ACES AUTOWRITE-------------------------------------
#TOOL DO IT FOR ANIMA FILMS PIPELINE#
#BASE IN PIPELINE ANIMA FILMS#

import nuke

def easyRenderRoot():
    easyRenderRoot = "L:/RDS/VFX01/SEQ"
    return easyRenderRoot

def autowritePNG():
    loadRoot = easyRenderRoot()
    writeMagic = nuke.createNode("Write")
    writeMagic['channels'].setValue("rgba")
    writeMagic.knob('colorspace').setValue(12)
    writeMagic.knob('file').setValue(easyRenderRoot() + '[string range [file tail [knob root.name]] 0 6]/02 OUT/LOW/PNG/[string range [file tail [knob root.name]] 0 11 ]_####.png')
    writeMagic.knob('create_directories').setValue(True)

def autowriteMOV():
    loadRoot = easyRenderRoot()
    writeMagic = nuke.createNode("Write")
    writeMagic['channels'].setValue("rgba")
    writeMagic.knob('file').setValue(easyRenderRoot() + '[string range [file tail [knob root.name]] 0 6]/02 OUT/LOW/MOV/[string range [file tail [knob root.name]] 0 11 ].mov')
    writeMagic.knob('colorspace').setValue(111)
    writeMagic.knob('meta_codec').setValue(4)
    writeMagic.knob('create_directories').setValue(True)


def autowriteEXR():
    shuffle = nuke.createNode("Shuffle")
    nuke.Layer('rgba', ['red', 'green', 'blue', 'alpha'])
    shuffle['out'].setValue('rgba')
    shuffle['alpha'].setValue(6)
    loadRoot = easyRenderRoot()
    writeMagic = nuke.createNode("Write")
    writeMagic['channels'].setValue("rgba")
    writeMagic.knob('file').setValue(easyRenderRoot() + '[string range [file tail [knob root.name]] 0 6]/02 OUT/HIGH/[string range [file tail [knob root.name]] 0 11 ]/[string range [file tail [knob root.name]] 0 11 ]_####.exr')
    writeMagic.knob('colorspace').setValue(12)
    writeMagic.knob('write_ACES_compliant_EXR').setValue("True")
    writeMagic.knob('create_directories').setValue(True)

def autowritePreRender():
    loadRoot = easyRenderRoot()
    prName = nuke.getInput('PreRender Name:', 'PreRender01')
    writeMagic = nuke.createNode("Write")
    writeMagic['channels'].setValue("rgba")
    writeMagic.knob('colorspace').setValue(12)
    writeMagic.knob('file').setValue(easyRenderRoot() + '[string range [file tail [knob root.name]] 0 6]/04 PRERENDERS/{}/{}_####.exr'.format(prName, prName))
    writeMagic.knob('create_directories').setValue(True)
