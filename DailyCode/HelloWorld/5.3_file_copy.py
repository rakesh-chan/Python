#copy text from one file to another

file1_name = input("Enter the filename to copy: ")
file1_info = open(file1_name+".txt")
file1_content = file1_info.read()

file2_name = input("Enter the destination file name to copy:")
file2_info = open(file2_name+".txt", 'w')
file2_info.write(file1_content)
file1_info.close()
file2_info.close()

x = input("Do u wanna confirm the copy? (Y/N)")

if (x == 'Y'):
    file2_info = open(file2_name+".txt")
    file2_content = file2_info.read()
    print ("size of the file is ", (len(file2_content)), " and content is ", file2_content)
    file2_info.close()
elif (x == 'N'):
    print ("Good Bye!!!")
    



