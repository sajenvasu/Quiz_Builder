# Version 1.0.1

from Printer_File import Print_Same_Line

def Version():
    Print_Same_Line(13, "*")
    print("Version 1.0.1")
    Print_Same_Line(13, "*")

print("******Menu******")
print("1) Take a Quiz")
print("2) Create a Quiz")
print("3) Modify a Quiz")
print("4) Version")
print("5) Exit")
inp = int(input("****************\n>> "))

print("")
if inp < 1 or inp > 5:
    print("Range not between 1 and 5")
elif inp == 1:
    #Take()
    print("")
elif inp == 2:
    #Create()
    print("")
elif inp == 3:
    #Modify()
    print("")
elif inp == 4:
    Version()
