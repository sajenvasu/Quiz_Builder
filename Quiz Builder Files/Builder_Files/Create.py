# First check if Builder_Data Directory exists
# IF Builder_Data exists then skip ELSE make the directory

from Directory_File import Check_Dir, Check_SizeofDir

Check_Dir()

if (Check_SizeofDir() != 0):
    print("Quizzes: " + str(Check_SizeofDir()))
    import View

    
    View 
    inp = int(input(">> "))

else:
    print("Quizzes: " + str(Check_SizeofDir()))