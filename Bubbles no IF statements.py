#Your assignment is to write the program for a Bubble Sort in Python.
#You should ask the user to input 5 numbers, sort the list of numbers-
#they give you and then display the list in the correct order.
#Before you start your code, think it through and come up with a plan.
#You know some things:  
#You know you need some variables to work with
#You have 5 numbers (if you do something a fixed amount of times…)
#You know you need some IF statements

import random

#Request name from user, return greeting.
name=input("Enter name: ")
print("Hello" + ", " + name + "!" "\n")

#Request user to input 5 numbers. (Space included)

print("Please enter 5 numbers:(spaces included)")
nums=list(map(int, input().split()))
nums.sort()

#Output numbers in order, given by user above.
print("Here are your numbers in order! ")
print(*nums)

#Prompt user to close program. (Ensures affirmation; program closed properly)
name=input("Press Enter again to close!")
print(name)
