
# Alexander J. Jackson
# locker_combonation.py

import random

def lockerCombo():
    myName = input("Enter your first name: ")
    num1 = random.randint(0,39)
    num2 = random.randint(0,39)
    num3 = random.randint(0,39)

    if num1 == num2 or num1 == num3 or num2 == num3:
        print()
        print(f"{myName}'s locker combination is: {num1}-{num2}-{num3}")
        print("Please try again, this is not a valid combination")
        lockerCombo()

    else:
        print()
        print(f"{myName}'s locker combination is: {num1}-{num2}-{num3}")
        print("This combination will work")


lockerCombo()
