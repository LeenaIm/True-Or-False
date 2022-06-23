

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
    print ("For this game you will be asked to...") 
    print ()
    print ("- Select the amount of rounds you would like to play")
    print ("- The computer will then generate a series of maths questions from addition, subtraction, multiplication or division")
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

# Main routine goes here...

statement_generator ("Welcome to Truth Or False - Maths edition", "*")
print ()

played_before = yes_no ("Have you played the game before? ")
if played_before == "no":
    instructions ()

print ()
print ("Let's get started...")
print ()
