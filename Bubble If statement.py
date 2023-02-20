#Your assignment is to write the program for a Bubble Sort in Python.
#You should ask the user to input 5 numbers, sort the list of numbers-
#they give you and then display the list in the correct order.
#Before you start your code, think it through and come up with a plan.
#You know some things:  
#You know you need some variables to work with
#You have 5 numbers (if you do something a fixed amount of times…)
#You know you need some IF statements

name=input("Enter Name:")
print("Hello" + ", " + name + "! \n" )

#Prompt user to input their desired numbers.
print("Please input a number and press enter each time: ") 

#Each variable per integar needed.
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
d = float(input("Enter fourth number: "))
e = float(input("Enter fifth number: "))

#pass through as ascending sorted order. If logic
if a > b:
    a,b = b,a
if a > c:
    a,c = c,a
if b > c:
    b,c = c,b
if b > d:
    b,d = d,b
if c > d:
    c,d = d,c
#if e > d:
    #e,d = d,e
#if d > e:
    #d,e = e,d
#else:
    #print (a, "<", b, "<", c, "<", d, "<", e)
print("Here are your numbers in order! \n")
print (a, "<", b, "<", c, "<", d, "<", e)

name=input("Press Enter to close program")