#read from file

from sys import argv

script,file_name = argv

txt = open(file_name)

print("Here is your file %r" %(file_name))
print(txt.read())
