#---------------------------------------------------------
#ReplaceFileName.py
#Version 1.0.9
#Last Update 20/07/20
#Francisco Biancardi
#---------------------------------------------------------------------------------------------------------
import nuke
import os
import shutil

def replaceFileName():

#-------------------------Panel Creation---------------------------
    p = nuke.Panel('Rename File Tool')
    p.addFilenameSearch('file path', "")
    p.addSingleLineInput('New Name', "new file name")
    p.addBooleanCheckBox('Save Copy', False)

    ret = p.show()

#---------------------------Definitions from the Path------------------------------
    if ret == True:

        inputPath = p.value('file path') #C:/Users/franc/OneDrive/Escritorio/folderA/casa/scene17_side_###.dpx 1-10
        newFileName = p.value('New Name')#"elnombreNuevo"
        basepath = os.path.dirname(inputPath)#C:/Users/franc/OneDrive/Escritorio/folderA/casa
        main_Name = '_'.join(os.path.splitext(os.path.basename(inputPath))[0].split('_')[:-1])#scene17_side_
        main_Extension = ''.join(os.path.splitext(inputPath)[-1].split(' ')[-2])#.dpx

#-------------------------Security Folder Creation------------------------------------
        if p.value('Save Copy') == True:
            SecurityFolder = os.path.join(basepath, "old_" + main_Name).replace('\\', '/')
            os.mkdir(SecurityFolder)
        else:
            print "there is no security folder"

#------------------Loop for each File in folder---------------------------------

        for f in os.listdir(basepath): #informacion aplicada a cada archivo
            file_name, file_ext = os.path.splitext(f)#['scene17_side_234', 'dpx']
            fileMainName, frameNumber = file_name.split('_')[:-1], file_name.split('_')[-1]#['scene17_side', '234']
            theName = '_'.join(fileMainName)
            oldName = '_'.join(fileMainName) + "_" +  frameNumber + file_ext
            newName = newFileName + "_" + frameNumber + file_ext
            FileOriginal = os.path.join(basepath, oldName).replace('\\', '/')
            NewFileName = os.path.join(basepath, newName).replace('\\', '/')

            if main_Name == theName and main_Extension == file_ext:
                if p.value('Save Copy') == True:
                    securitySavePath = os.path.join(SecurityFolder, oldName).replace('\\', '/')
                    shutil.copyfile(FileOriginal, securitySavePath)
                else:
                    print "there is no security copy to do here"

                os.rename(FileOriginal, NewFileName)

            else:
                print  "this file: {} is not for rename or copy".format(oldName)

    else:
        print "cagaste"
        return
