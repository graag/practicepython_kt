name = input("Hello! Please type in your name: ")
age = int(input("And your age: "))
copies = int(input("No. of copies: "))

message = "Dear " + name + ", in " + str(2118 - age) + " you will be 100 years old!\n"
print(copies * message)
