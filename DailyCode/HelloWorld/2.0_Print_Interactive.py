#print with raw input

print("Press 1: To print")
print("Press 2: To combine two strings")
print("Press 3: To print in sperate lines")
print("Press 4: To print your entered string and digit")
print("Press 5: To print multiple times")

x = int(input())

if (x==1):
    print(input("Enter the string to combine : "))

elif(x==2):
    str1 = input("enter line 1: ")
    str2 = input("enter line2: ")
    print (str1+" "+str2)

elif(x==3):
    str1 = input("enter line 1: ")
    str2 = input("enter line2: ")
    print (str1+"\n"+str2)
    
elif(x==4):
    str1 = input("enter string : ")
    var1 = int(input("enter numeric: "))
    print ("your string is %s and number is %d" %(str1,var1))
    print("your string is " ,str1, " and your number is " ,var1)

elif (x==5):
    str1 = input("Enter string to print: ")
    str2 = str1 + " "
    var1 = int(input("Number of times to print: "))
    print(str2 * var1)
else:
    print("Invalid Input")
