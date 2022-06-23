import random

num1 = random.randint(1, 10)

num2 = random.randint(1, 10)

answer = int(input("What is {num1} + {num2}?\n"))

if answer == (num1 + num2):
    print("Correct")

else:
    print("Wrong")