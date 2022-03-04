from Directory_File import List_FilesinDir, Check_SizeofDir

listFiles = List_FilesinDir()
sizeofQuizzes = Check_SizeofDir()
len_sizeofQuizzes = len(str(sizeofQuizzes + 1))
concate_listFiles = []

for x in range(len(listFiles)):
    len_currentQues = len(str(x+1))
    num_spaces = (len_sizeofQuizzes - len_currentQues)
    spaces = num_spaces * " "
    insertDataToList = str(x+1) + ": " + spaces + str(listFiles[x])
    print(insertDataToList)