import random
import math

# If they say yes, output 'Let's get started...'
# If they say no, output '*** How To Play ***'
# If the answer is invalid, 'Please answer yes / no'
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

# Instructions - how to play game
def instructions() :
    print ()
    print ("**** How To Play ****")
    print ()
    print ("Welcome to Truth Or False - Maths edition")
    print ()
    print ("This game will...") 
    print ()
    print ("- First ask you how many questions of true or false you would like to play")
    print ("- Then the computer will then generate a series of addition only math questions from 1 - 100")
    print ("- Your objective is to guess if the question is either true or false")
    print ("- Enter true / false or t / f")
    print ()
    print ("*** Good luck! ***")

# Statement generator 
def statement_generator (statement, decoration) :

    sides = decoration * 3

    statement = " {} {} {} ".format (sides, statement, sides)
    top_bottom = decoration * len (statement)

    print (top_bottom)
    print (statement)
    print (top_bottom)

    return ""

# Checks user enter an integer that is more than 0
def check_rounds ():
    while True:
        response = input ("How many questions would you like: ")

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

# Choice checker
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

# Main routine goes here...

game_summary = [] 
game_guess_history = []

rounds_lost = 0
rounds_played = 0
rounds_played = 0

statement_generator ("Welcome to Truth Or False - Maths edition", "*")
print ()

# asks user if they have played, if no displays introduction, if yes game continues

played_before = yes_no ("Have you played the game before? ")
if played_before == "no":
    instructions ()

print ()
print ("Let's get started...")
print ()

# Main routine goes here...

rounds_played = 0
choose_instruction = "True Or False: "
user = check_rounds

guess = ""

# Ask user for # of rounds and check if valid, <enter> for infinite mode
rounds = check_rounds ()

end_game = "no"
while end_game == "no":

    # Start of Game Play Loop

    # question generator, randomizes equations between 1 - 20

    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    num3 = random.randint(1, 20)

    print()
    question = "{} + {}".format(num1, num2)

    actual_answer = num1 + num2
    false_answer = actual_answer + num3

    true_question = eval("{} == {}".format(actual_answer, question))
    ("True", true_question)

    false_question = eval("{} == {}".format(actual_answer, num3))
    ("False", false_question)

    # Rounds Heading (shows round for continuous or round / of total rounds for regular mode)

    if rounds == "":
        heading = "Continiuous Mode: Round {}".format (rounds_played + 1)
    else:
        heading = "Question {} of {}:".format (rounds_played +1, rounds)

    print (heading)
    print ()

    # Generating true questions with correct answers
    # If user enters true and answer is true, prints "well done!"
    # If user enters anything other than true, prints "Sorry the correct answer was true"

    answer = input("{} = {} - True or False: ".format (question, actual_answer))

    if answer == 'true' or answer == 't': 
        print ()
        print("Well done! The answer was true :)")

    else:
        print ()
        print("Sorry, the correct answer was true :(")

    # End game if exit code is typed
    if guess == "xxx":
        break

    rounds_played += 1

    if rounds_played == rounds:
        end_game = "yes"

    # **** rest of loop / game *****
