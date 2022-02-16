import subprocess
import platform

os_name = platform.system()

if (os_name == "Windows"):
    print("Windows")

elif(os_name == "Linux"):
    subprocess.call("clear && python Quiz\ Builder\ Files/Builder_Files/RUN.py", shell = True)
    subprocess.call("cd Quiz\ Builder\ Files/Builder_Files/__pycache__/ && rm *", shell = True)
    subprocess.call("cd Quiz\ Builder\ Files/Builder_Files/ && rmdir __pycache__", shell = True)