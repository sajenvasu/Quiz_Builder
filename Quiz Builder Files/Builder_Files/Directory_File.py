import os
import platform

path = os.getcwd()
Linux_newPath = path + "/Quiz Builder Files/Builder_Data"
Windows_newPath = path.replace("Builder_Files", "Builder_Data")

def Check_Dir():
    if (platform.system() == "Linux"):      
        if not(os.path.isdir(Linux_newPath)):
            os.mkdir(Linux_newPath)
            
    if (platform.system() == "Windows") and not(os.path.isdir(Windows_newPath)):
            os.mkdir(Windows_newPath)

def Check_SizeofDir():
    if (platform.system() == "Linux"):
        x = len(os.listdir(Linux_newPath))
        return x
    elif (platform.system() == "Windows"):
        x = len(os.listdir(Windows_newPath))
        return x

def List_FilesinDir():
    if (platform.system() == "Linux"):
        list_ofQuiz = os.listdir(Linux_newPath)
        return list_ofQuiz
    elif (platform.system() == "Windows"):
        list_ofQuiz = os.listdir(Windows_newPath)
        return list_ofQuiz