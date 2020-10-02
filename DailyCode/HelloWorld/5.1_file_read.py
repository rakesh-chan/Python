#read the file using user prompt

file_name = input("Enter the file name:")
txt = open(file_name+".txt")
print(txt.read())
