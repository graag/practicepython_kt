import datetime

name = input("Hello! Please type in your name: ")
age = int(input("And your age: "))
copies = int(input("No. of copies: "))

year = datetime.datetime.now().year

message = "Dear " + name + ", in " + str(year - age + 100) + " you will be 100 years old!\n"
print(copies * message)
