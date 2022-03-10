
#Joel Lantigua 00294961
#Mini Project
#Programing for IT CIS-153
#This is a simple math quiz that generates random number for the questions



# Introduction

name = input("Hello Welcome Please Enter your full name:")
quiz = input("Hello " + name + " Would you like to take a quiz? Yes or No:")


score = 0



if quiz == "y":
    print("Okay " + name + " we will begin a math quiz! ")

print("     ")

#question 1 multiplication 

import random

x = random.randint(1, 10)
y = random.randint(1, 10)

print("Please Answer the following qusetion " + str(x)+ " * " + str(y) + ":")
answer = int(input("What's the answer: "))
if answer == (x * y):
    print(" This is correct moving on!")
    score = score + 25
else:
    print("The answer you provided is Wrong!! The correct answer is " + str(x * y))



print("     ")

#question 2 this wil be Division


import random

A = random.randint(1, 10)
B = random.randint(1, 10)

print(" The next qusetion will be division " + str(A)+ " / " + str(B) + ":")
answer = (input("What's the answer: "))
if answer == (A / B):
    print(" This is correct moving on!")
    score = score + 25
else:
    print("The answer you provided is Wrong!! The correct answer is " + str(A / B))

print("     ")


#question 3 what is the remainder?



import random

C = random.randint(1, 10)
D = random.randint(1, 10)

print(" This next qusetion you will be finding the remandier " + str(C)+ " % " + str(D) + ":")
answer = int(input("What's the answer: "))
if answer == (C % D):
    print(" This is correct moving on!")
    score = score + 25
else:
    print("The answer you provided is Wrong!! The correct answer is " + str(C % D))

print("     ")


#question 4 exponets 


import random

E = random.randint(1, 10)
F = random.randint(1, 10)

print(" This last next qusetion will be exponets  " + str(E)+ " ^ " + str(F) + ":")
answer = int(input("What's the answer: "))
if answer == (E ** F):
    print(" This is correct Thank You for taking this quiz!")
    score = score + 25
else:
    print("The answer you provided is Wrong!! The correct answer is " + str(E ** F))

print("     ")

print("The End Thank You " +  name + " For Taking This Quiz!!")

print("     ")

# score print

print("your score is " + str(score) + "%")

