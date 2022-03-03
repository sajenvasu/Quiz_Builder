from Directory_File import Check_SizeofDir, Print_FilesinDir
from Printer_File import Print_Same_Line, Print_Same_New_Line, Print_String_Evenly_Same_Line

list_ofQuiz = Print_FilesinDir()

len_longest_Quizname = -1
key_longest_Quizname = -1

def Check_Longest_Path():
    len_temp = 0
    for x in range(len(list_ofQuiz)):
        if (len(list_ofQuiz[x]) > len_temp):
            # print(list_ofQuiz[x])
            # print(x)
            len_temp = len(list_ofQuiz[x])
            len_longest_Quizname = len_temp
            print(len_temp)
            # key_longest_Quizname = x


Check_Longest_Path()
title_ListofQuiz = "List of Quizzes"
len_QuizList = len(str(Check_SizeofDir()))
final_length_size = len_longest_Quizname


Print_Same_New_Line(final_length_size, "*")
Print_String_Evenly_Same_Line(title_ListofQuiz, final_length_size, " ")
Print_Same_New_Line(final_length_size, "*")
    


for x in range(len(list_ofQuiz)):
    print(str(x+1) + ":", end = "")
    Print_Same_Line((len_QuizList + 1) - len(str(x+1)), " ")
    print(str(list_ofQuiz[x]))

Print_Same_New_Line(final_length_size, "*")