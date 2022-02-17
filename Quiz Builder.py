import subprocess
import platform

os_name = platform.system()

if (os_name == "Windows"):
    subprocess.call("cls && cd Quiz Builder Files\Builder_Files && python RUN.py", shell = True)

elif(os_name == "Linux"):
    subprocess.call("clear && python3 Quiz\ Builder\ Files/Builder_Files/RUN.py", shell = True)
    subprocess.call("cd Quiz\ Builder\ Files/Builder_Files/__pycache__/ && rm *", shell = True)
    subprocess.call("cd Quiz\ Builder\ Files/Builder_Files/ && rmdir __pycache__", shell = True)