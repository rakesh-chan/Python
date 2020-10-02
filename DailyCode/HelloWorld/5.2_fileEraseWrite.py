#Write to a file after deleteing whats existing

file = input("Enter the file name: ")
txt = open(file+".txt", 'r')
print (txt.read())
erase = input("DO u wanna erase the file(Y/N)?")

if (erase == 'Y'):
    print ("Truncating file .....")
    txt = open(file+".txt", 'w')
    txt.truncate()
    line = input ("Enter new message")
    txt.write(line)
    txt.close()
    txt = open(file+".txt", 'r')
    print (txt.read())
elif (erase == 'N'):
    print ("file not erased..")
    txt = open(file+".txt", 'r')
    print (txt.read())
