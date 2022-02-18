from Directory_File import Print_FilesinDir
list_ofQuiz = Print_FilesinDir()

from Printer_File import Print_Same_Line, Print_String_Evenly_Same_Line

title_ListofQuiz = "List of Quizzes"
Print_Same_Line(len(max(list_ofQuiz, key=len)) + 3, "*")
Print_String_Evenly_Same_Line(title_ListofQuiz, len(max(list_ofQuiz, key=len)) + 3, " ")
Print_Same_Line(len(max(list_ofQuiz, key=len)) + 3, "*")

for x in range(len(list_ofQuiz)):
    print(str(x+1) + ": " + str(list_ofQuiz[x]))

Print_Same_Line(len(max(list_ofQuiz, key=len)) + 3, "*")