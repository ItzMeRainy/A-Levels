# Importing methods and procedures from a module File. (Here I have only imported a single method since I do not need anything else)
from random import randint

# Writing a program to check if randomly generated numbers is odd or even.
MyNumber = randint(1, 10)

if MyNumber % 2 == 0:
    print("Even")
else:
    print("Odd")