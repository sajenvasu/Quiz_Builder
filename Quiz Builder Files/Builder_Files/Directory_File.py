import os
import platform

path = os.getcwd()
Linux_newPath = path + "/Quiz Builder Files/Builder_Data"

def Check_Dir():
    if (platform.system() == "Linux"):      
        if not(os.path.isdir(Linux_newPath)):
            os.mkdir(Linux_newPath)

def Check_SizeofDir():
    if (platform.system() == "Linux"):
        x = len(os.listdir(Linux_newPath))
        return x

def Print_FilesinDir():
    if (platform.system() == "Linux"):
        list_ofQuiz = os.listdir(Linux_newPath)
        return list_ofQuiz