from Directory_File import Check_Dir, Check_SizeofDir
Check_Dir()

if (Check_SizeofDir() != 0):
    import View
    
    View 
    inp = int(input("[Enter Quiz To Take] >> "))

else:
    print("[Please create a quiz to Take]")