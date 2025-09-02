
file1  = open("output.txt","w")
a = str(input("Enter text to write to the file: "))
print("Data successfully written to output.txt.")
file1.write(a + "\n")
file1.close()

file1 = open("output.txt", "a")
b = str(input("Enter additional text to append: "))
print("Data successfully appended.")
file1.write(b)
file1.close()

file1 = open("output.txt", "r")
print("Final content of out.txt: ")
file_read = file1.read()
print(file_read)