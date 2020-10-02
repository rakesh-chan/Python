#copy text from one file to another

from os.path import exists

def copy_confirm():
    x = input("Do u wanna confirm the copy? (Y/N)")

    if (x == 'Y'):
        file2_info = open(file2_name+".txt")
        file2_content = file2_info.read()
        print ("size of the file is ", (len(file2_content)), " and content is %r" %file2_content)
        file2_info.close()
    elif (x == 'N'):
        print ("Good Bye!!!")
def copy_confirm1():
    x = input("Do u wanna confirm the copy? (Y/N)")

    if (x == 'Y'):
        file1_info = open(file1_name+".txt")
        file1_content = file1_info.read()
        print ("size of the file is ", (len(file1_content)), " and content is %r" %file1_content)
        file1_info.close()
    elif (x == 'N'):
        print ("Good Bye!!!")

file1_name = input("Enter the filename to copy: ")
file1_exist = exists(file1_name+".txt")

if (file1_exist == False):
	y = input("Do u wanna create a new copy? (Y?N)")
	if (y == 'Y'):
		file1_content = input("Enter the message:")
		file1_info = open(file1_name+".txt", 'w')
		file1_info.write(file1_content)
		file1_info.close()
		copy_confirm1()
	else:
		print ("Cancelled")
else:
    file1_info = open(file1_name+".txt")
    file1_content = file1_info.read()
    file2_name = input("Enter the destination file name to copy:")
    file2_exist = exists(file2_name+".txt")
      
    if ((file2_exist == True) and (file1_name == file2_name) ):
        overwrite = input("Confirm Overwriting (Y/N): ")
        if (overwrite == 'Y'):
            over_content = input("Enter message: ")
            file2_info = open(file2_name+".txt", 'w')
            file2_info.write(over_content)
            file1_info.close()
            file2_info.close()
            copy_confirm()
        else:
            print ("Overwriting Cancelled")

    
    elif (file2_exist == True):
        print("output file exists?", exists(file2_name+".txt"))
        file2_info = open(file2_name+".txt", 'w')
        file2_info.write(file1_content)
        file1_info.close()
        file2_info.close()
        copy_confirm()

    else:
        y = input("Do u wanna create a new copy? (Y?N)")
        if (y == 'Y'):
            file2_info = open(file2_name+".txt", 'w')
            file2_info.write(file1_content)
            file1_info.close()
            file2_info.close()
            copy_confirm()
        else:
            print ("Copying Cancelled")



    



