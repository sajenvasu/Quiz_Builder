from Directory_File import Check_Dir, Check_SizeofDir
Check_Dir()

if (Check_SizeofDir() != 0):
    import View
    
    View 
    inp = int(input(">> "))

else:
    print("[Please Create A Quiz To Take]")