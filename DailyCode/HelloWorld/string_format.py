
for i in range(1,13):
    print("square of {0} is {1} and cube of {0} is {2}".format(i,i**2,i**3))

meal1 = "spam" + "eggs" + "beans"
meal2 = "spam\neggs\nbeans"
meal3 = "spam, eggs, beans"
meal4 = """spam
eggs
beans"""

print(meal1)
print(meal2)
print(meal3)
print(meal4)

days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
print(days[::5])

data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"

print(data[::5])
print(data[1:5])
print(data[0:-1:5])
print(data[:-1:5])
