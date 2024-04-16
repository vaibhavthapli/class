'''
1. Without Parameters, without Return
2. With Parameters, without Return
3. Without PArameters, with Retrun
4. With Parameters, with Return
'''

#parameters and Arguments
def addition(n1,n2):#parameters
    total = n1 + n2
    print(total)
addition(1,2)
addition("vai","tha")#arguments

def addition_list(x):
    total = 0
    for i in x:
        total = total + i
    print(total)
my_list = [5,6,7,3,2]
addition_list(my_list)

#return
def addition1(n1,n2):
    total = n1 + n2
    return total
x =addition1(10,20)
print(x)
print(addition1(10,20))

#Example
# Q: Ask 2 numer from user calculate total of 2 numbers then print if the sum is odd or even
# using add and check

def add(n1,n2):
    total = n1 + n2
    return total

def check(num):
    if num%2==0:
        return "Even"
    else:
        return "odd"

x = int(input("Enter n1: "))
y = int(input("Enter n2: "))
s = add(x,y)
print(check(s))