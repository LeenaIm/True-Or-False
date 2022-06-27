import random
import math

def yes_no (question) :

    valid = False
    while not valid:
        response = input (question) .lower()

        if response == "yes" or response == "y" :
            response = "yes"
            return response

        elif response == "no" or response == "n" :
            response = "no" 
            return response

        else:
            print ()
            print ("Please answer yes / no")
            print ()

def instructions() :
    print ()
    print ("**** How To Play ****")
    print ()
    print ("Welcome to Truth Or False - Maths edition")
    print ("This game will...") 
    print ()
    print ("- Give you ")
    print ("- The computer will then generate a series of maths addition questions")
    print ("- Your objective is to guess if the question is either true or false")
    print ("- Enter true / false or t / f")
    print ()
    print ("*** Good luck! ***")

def statement_generator (statement, decoration) :

    sides = decoration * 3

    statement = " {} {} {} ".format (sides, statement, sides)
    top_bottom = decoration * len (statement)

    print (top_bottom)
    print (statement)
    print (top_bottom)

    return ""

def choice_checker (question, valid_list, error):

    valid = False
    while not valid:

        # Ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        # iterates through list and if response is an item
        # in the list (or the first letter of an item), the
        # full item name is returned
        
        for item in valid_list:
            if response == item [0] or response == item:
                return item

        # output error if item not in list 
        print (error)
        print ()
            
def check_rounds ():
    while True:
        response = input ("How many rounds: ")

        round_error = "Please type either <enter> or an integer that is more than 0"
        if response != "":
            try:
                response = int (response)

                if response < 1:
                    print (round_error)
                    continue

            except ValueError:
                print (round_error)
                continue

        return response

# Main routine goes here...

rounds_lost = 0
rounds_played = 0
rounds_played = 0

GUESSES_ALLOWED = 5

mode = "regular"

statement_generator ("Welcome to Truth Or False - Maths edition", "*")
print ()

played_before = yes_no ("Have you played the game before? ")
if played_before == "no":
    instructions ()

print ()
print ("Let's get started...")

print (check_rounds)













