from random import sample
try:

    file1 = open("sample.txt","r")
    print("Reading file content")
    file_read = file1.readline()
    print("Line 1: " , file_read)
    file_read1 = file1.read()
    print("Line 2: ", file_read1)


except FileNotFoundError:
    print("The file 'sample.txt' was not found")
