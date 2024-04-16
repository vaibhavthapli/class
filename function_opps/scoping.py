def addition():
    num1 = int(input("Enter num 1= "))
    num2 = int(input("Enter num 2= "))
    print(f"Answer = {num1 + num2}")

addition()

def subtraction():
    num1 = int(input("Enter num 1= "))
    num2 = int(input("Enter num 2= "))
    print(f"Answer = {num1 - num2}")
subtraction()
#scoping: variables in function only work inside that function

def greet():
    name = input("Enter your name: ")
    print(f"Your name is {name}")
name = "xyz"
greet()
print(name)
'''
output: 
Enter your name: VAibhav
Your name is VAibhav
xyz
'''