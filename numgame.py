#!/usr/bin/env python3

import random


# THIS FUNCTION DETERMINES THE LARGEST NUMBER OUT OF A GIVEN LIST OF NUMBERS
def largestnum():
    print("In this game you or the computer will choose ten random numbers, print them and tell you which one is the largest")
    decide = input("Do you want to choose the numbers yourself?(Y/N)")
    rand_nums = [
            random.randint(0, 1000000),
            random.randint(0, 1000000),
            random.randint(0, 1000000),
            random.randint(0, 1000000),
            random.randint(0, 1000000),
            random.randint(0, 1000000),
            random.randint(0, 1000000),
            random.randint(0, 1000000),
            random.randint(0, 1000000),
            random.randint(0, 1000000),
    ]

    
    largest = None

    if decide == "Y":
        nums = [
            int(input("number 1: ")),
            int(input("number 2: ")),
            int(input("number 3: ")),
            int(input("number 4: ")),
            int(input("number 5: ")),
            int(input("number 6: ")),
            int(input("number 7: ")),
            int(input("number 8: ")),
            int(input("number 9: ")),
            int(input("number 10: "))
        ]

        for number in nums:
            if largest == None or largest < number:
                largest = number
        print("The largest number is", largest)

    elif decide == "N":
        for num in rand_nums:
            if largest == None or largest < num:
                largest = num
        print("The largest number is", largest)
    else:
        while decide != "Y" or decide != "N":
            print("Please answer with Y or N")
            decide = input("Do you want to choose the numbers yourself?(Y/N)")
            if decide == "Y" or decide =="N":
                largestnum() 
                if input("Do you want to exit?(Y/N)") == "Y":
                    return
                elif input("Do you want to exit?(Y/N)") == "N":
                    largestnum()
                return
            return
                
                





# THIS FUNCTION DETERMINES THE SMALLEST NUMBER IN A GIVEN LIST OF NUMBERS
def smallestnum():
    print("In this game you or the computer will choose ten random numbers, print them and tell you which one is the smallest")
    decide = input("Do you want to choose the numbers yourself?(Y/N)")
    rand_nums = [
            random.randint(0, 1000000),
            random.randint(0, 1000000),
            random.randint(0, 1000000),
            random.randint(0, 1000000),
            random.randint(0, 1000000),
            random.randint(0, 1000000),
            random.randint(0, 1000000),
            random.randint(0, 1000000),
            random.randint(0, 1000000),
            random.randint(0, 1000000),
    ]

    
    smallest = None

    if decide == "Y":
        nums = [
            int(input("number 1: ")),
            int(input("number 2: ")),
            int(input("number 3: ")),
            int(input("number 4: ")),
            int(input("number 5: ")),
            int(input("number 6: ")),
            int(input("number 7: ")),
            int(input("number 8: ")),
            int(input("number 9: ")),
            int(input("number 10: "))
        ]

        for number in nums:
            if smallest == None or smallest > number:
                smallest = number
        print("The smallest number is", smallest)

    elif decide == "N":
        for num in rand_nums:
            if smallest == None or smallest < num:
                smallest = num
        print("The smallest number is", smallest)
    else:
        while decide != "Y" or decide != "N":
            print("Please answer with Y or N")
            decide = input("Do you want to choose the numbers yourself?(Y/N)")
            if decide == "Y" or decide =="N":
                smallestnum() 
                if input("Do you want to exit?(Y/N)") == "Y":
                    return
                elif input("Do you want to exit?(Y/N)") == "N":
                    smallestnum()
                return
            return



def numguesser():
    randnum = random.randint(1, 100)
    print("In this game you have to guess the computer generates a random number between 1 and 100 and you have to guess the right one.")
    print("You have 3 guesses.")
    guess1 = int(input("What's your first guess? "))
    if guess1 == randnum:
        print("That is correct, congrats!")
    else:
        print("False, try again!")
    guess2 = int(input("What's your second guess? "))
    if guess2 == randnum:
        print("That is correct, congrats!")
    else:
        print("False, the next guess is your last one so be careful")
    guess3 = int(input("This is your third and last guess so think about it carefully! "))
    if guess3 == randnum:
        print("That's right, you won the game!")
    else:
        print("You lost the game unfortunatly!")
        redo = input("Do you want to try again with another number?(Y/N) ")
        if redo == "Y":
            numguesser()



choice = int(input("Which game do you want to play?(1/2/3)\n 1) largest number guesser\n 2) smallest number guesser\n 3) random number guesser\n\n"))

if choice == 1:
    largestnum()
elif choice == 2:
    smallestnum()
elif choice == 3:
    numguesser()
