def Check_Dir():
    import os
    import platform

    if (platform.system() == "Linux"):
        path = os.getcwd()
        new_path = path + "/Quiz Builder Files/Builder_Data"
        
        if not(os.path.isdir(new_path)):
            os.mkdir(new_path)