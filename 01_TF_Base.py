import random
import math
from tabnanny import check

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
    print ("- The computer will then generate a series of maths questions")
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

def intcheck(question, low=None, high=None, exit_code = None):

    while True:

        # sets up error messages
        if low is not None and high is not None:
            error = "Please enter an integer between {} and {} (inclusive)".format(low, high)
        elif low is not None and high is None:
            error = "Please enter an integer that is more than or equal to {}".format(low)
        elif low is None and high is not None:
            error = "Please enter an integer that is less than or equal to {}".format(high)
        else:
            error = "Please enter an integer"

        try:
            response = input(question)
            
            # check to see if response is the exit code and return it
            if response == exit_code:
                return response
            
            # change the response into an integer
            else:
                response = int(response)

            # Checks response is not too low, not use of 'is not' keywords
            if low is not None and response < low:
                print(error)
                continue

            # Checks response is not too high
            if high is not None and response > high:
                print(error)
                continue

            return response

        # checks input is a integer
        except ValueError:
            print(error)
            continue

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

rounds_played = 0
round_error = ("Please choose how many questions would you like to play")

# Ask user for # of rounds..
print ()
rounds = intcheck("How many rounds or <enter> for infintite: ", 1, exit_code = "")

if rounds == "":
    print("You chose infinite mode")
    mode = "infinite"
    rounds = 5
else:
    print("You asked for {} rounds".format(rounds))

# Rounds Heading

end_game = "no"
while end_game == "no":

    
    result = "won"

    if rounds_played == rounds:
        break

    already_guessed = []
    guesses_left = GUESSES_ALLOWED

    if mode == "infinite":
        heading = "Continiuous Mode: Round {}".format (rounds_played + 1)
        rounds += 1
    else:
        print ()
        heading = "Round {} of {}".format (rounds_played + 1, rounds)
    print (heading)
    choose_instruction = "Please choose a lower number then higher number"
    choose_error = intcheck


# from random import choice
questions = ['questions 1', 'question 2', 'question 3']
random_item = random.choice(questions)

print (random_item)