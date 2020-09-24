#print examples

print ("This is a print format in python3") # python 2 works without paranthesis 
print ("This will print in \n next line")
print ('single quote print')
##############################################################


str1 = "string1"
str2 = "'%R' included"
var1 = 30
print("my string is %s and variable is %d" %(str1,var1))
print("my string is %r and variable is %d" %(str2,var1))
##############################################################


print ("i have a box of %s and the cost is %d" %("mango", 20))
##############################################################


print ("i am printing this 10 times continuosly. "*10)
print ("i am printing this 10 times line by line.\n"*10)
##############################################################


days = " Sun Mon Tue Wed Thu Fri Sat"
Months = "\nJan\nFeb\nMar\nApr\nMay\nJune\nJuly\nAug\nSep\nOct\nNov\nDec"

print ("Here are the days : " , days)
print ("Here are the months : ", Months)
print ("year consists of : ", days+Months)
print ("escaping \" in a sentance")
print ("\tTabbing it")
print ("b\a\c\k\s\l\a\s\h\i\n\g")
print ("b\\a\\c\\k\\s\\l\\a\\s\\h\\i\\n\\g")
