
# checks user enter an integer that is more than 0

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

# Main routine goes here...

rounds_played = 0
choose_instruction = "rewuyrwehuie"

# Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds ()

end_game = "no"
while end_game == "no":

    # Start of Game Play Loop


    # Rounds Heading (shows round for continuous or round / of total rounds for regular mode)
    print ()
    if rounds == "":
        heading = "Continiuous Mode: Round {}".format (rounds_played + 1)
    else:
        heading = "Question {} of {}".format (rounds_played +1, rounds)
    
    print (heading)
    choose = input ("{} or 'xxx' to end: ".format (choose_instruction))

    # Ask user for choice and check it's valid

    # End game if exit code is typed
    if choose == "xxx":
        break

    rounds_played += 1

    if rounds_played == rounds:
        end_game = "yes"

    # **** rest of loop / game *****