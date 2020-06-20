#---------------------------------------------------------
#hubCamera.py
#Version 1.0.0
#Last Update 19/06/20
#---------------------------------------------------------

import nuke
import os

def HubCamera():

###################CREATING DIRECTORY############################


#-----defining first part of the dinamic directory(based in nukeproject)--------

    scriptDirectory = nuke.script_directory()
    cutDirectory = scriptDirectory.split('/')
    eliminateVariable = []

    if os.path.isdir(scriptDirectory) == False:
        nuke.message("The nuke project it's not define" +" \n "+ "please save file")

    else:
        for x in cutDirectory:
            if x == 'Script':
                del x
            else:
                eliminateVariable.append(x)

        camDirectory = '/'.join(eliminateVariable) + "/Camera/"


#--------File search .abc or .fbx and store in camsAvailable----------

        if os.path.isdir(camDirectory) == False:
            nuke.message("out of the pipeline:" + "\n" + "expecting X:/Movie/Scene/Shot/Script/ - for the scripts files" + "\n" + "expecting X:/Movie/Scene/Shot/Camera/ - for the Camera files")
            return

        else:

            camsAvailable = [] ###all cameras availables###

            for filename in os.listdir(camDirectory):
                if filename.endswith(".abc") or filename.endswith(".fbx"):
                    camsAvailable.append(filename)
                else:
                    print "this is not a cam file {}".format(filename)

#--------------Appendin last camara file (by version)---------------

            lastCameraFile = []

            if len(camsAvailable) > 0:
                lastCameraFile.append(camsAvailable.pop())#ultima camara por version. pero puede fallar
                lastCameraFile = "".join(lastCameraFile)
            else:
                nuke.message("there are no camera in: " + "\n" + "{}".format(camDirectory))
                return
#---------------Camara creation and path confirm---------------------

            finallyThePath = camDirectory + lastCameraFile


###################CREATING CAMERA############################

            hubCamera = nuke.createNode("Camera2")
            hubCamera['read_from_file'].setValue(True)
            hubCamera['file'].setValue(finallyThePath)




#######NO HAY CAMARAS EN DIRECTORIO### ok
#######NO SE ENCUENTRA DIRECTORIO#####ok (eliminar doble mensaje)
#######NO ESTA DEFINIDO LA RUTA DEL NUKE##### ok
#######guardalo y reemplazar como archivo.###