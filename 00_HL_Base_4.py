from asyncore import loop
import random


# Funotions go here...
def check_rounds():
    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <enter> or an integer that is more than 0\n"

        # If infinite mode not chosen, check response is an integer that is more than 0
        if response != "":
            try:
                response = int(response)

                # If response is too low, go back to start of loop
                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response

def choice_checker(question, valid_list, error):

    valid = False
    while not valid:

        # Ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        # interates through list and if response is an item
        # in the list (or the first letter of an item), the full item 
        # name is returned

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        # output error if item not in list
        print(error)
        print()


# Main routine goes here

# Lists of valid responses 
yes_no_list = ["yes", "no"]

# ask user for # of rounds then loop...
game_summary = []

rounds_played = 0

# intialise lost / drawn counters
rounds_lost = 0

# Ask  user for # of rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # Start of Game Play Loop

    # Rounds Heading
    print()
    if rounds == "":
        heading = "Continuous Mode: Rounds {} (xxx to quit)".format(rounds_played + 1)
    else:
        heading = "Rounds {} of {}".format(rounds_played +1, rounds)

    print(heading)
    choose_instruction = "Please choose a number between 1 and 100 "
    choose_error = "Please choose a number between 1 and 100 (or xxx to quit)"

    # Ask user for choice and check it's valid
    user_choice = choice_checker(choose_instruction, choose_error)
    

    # End game if exit code is typed
    if user_choice == "xxx":
        print("***** Thanks for playing *****")
        break

# checks user has entered yes / no
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please answer yes / no") 

def instructions(): 
        print()
        print("You will be asked to pick 2 numbers between 1 & 100.")
        print()
        print("There will be a randomly generated number between the two numbers of your choice.")
        print()
        print("You'll be given 9 gusses to guess the random number.")
        print()
        return""

# makes the text look better, adds to the austhetics 
def statement_generator(statement, decoration, lines):

    sides = decoration * 3
    statement = "{} {} {}".format(sides, statement, sides)
    
    if lines == 1:
        print(statement)
    else:
        top_bottom = decoration * len(statement)

        print(top_bottom)
        print(statement)
        print(top_bottom)

    return ""

# Greets the player  
greeting = "Hello, and welcome to the higher or lower game."
sides = "*" * 3

greeting = "{} {} {}".format(sides, greeting, sides)

top_bottom = "*" * len(greeting)

print(top_bottom)
print(greeting)
print(top_bottom)

# Ask user if they have played before
show_instructions = yes_no("Would you like to see the instructions? ")

if show_instructions == "yes":
    instructions()

# HL component 5 - no duplicates

# To Do
# set up empty list called already_guessed
# when user guesses, add gues to list
# for each guess, check that number is not in already_guessed

# HL component 5 - Prevents duplicate guesses

# Functions go here

# Number Checking function goes here
def int_check(question, low=None, high=None):

    situation = ""

    if low is not None and high is not None:
        situation = "both"
    elif low is not None and high is None:
        situation = "low only"

    while True:

        try:
            response = int(input(question))

            # checks input is not too high or too low if a both upper and lower bounds are specified
            if situation == "both":
                if response < low or response > high:
                    print("Please enter a number between {} and {}".format(low, high))
                    continue
            # checks input is not too low
            elif situation == "low only":
                if response < low:
                    print("Please enter a number that is more than (or equal to) {}".format(low))
                    continue
            return response

        # checks input is a integer 
        except ValueError:
            print("Please enter an integer")
            continue



# Main routine goes here


GUESSES_ALLOWED = 9

already_guessed = []
guesses_left = GUESSES_ALLOWED
num_won = 0 

# Game setup, ask user for number of rounds etc


SECRET = random.randint(1, 100)

guess = ""

while guess != SECRET and guesses_left >= 1:

    guess = int_check("Guess: ")  # replace this with integer chcker

    # checks that guess is not a duplicate
    if guess in already_guessed:
        print("You already guessed that number! Please try again. You *still* have {} guesses left".format(guesses_left))
        continue

    guesses_left -= 1
    already_guessed.append(guess)

    if guesses_left >= 1:

        if guess < SECRET:
            print("Too low, try a higher number. Guesses left: {}".format(guesses_left))

        elif guess > SECRET:
            print("Too high, try a lower number. Guesses left: ")
    else:
        if guess < SECRET:
            print("Too low!")
        elif guess > SECRET:
            print("Too high!")
        

    if guess == SECRET: 
        if len(already_guessed) == 1:
            print("Amazing! you got it in the first attempt.")
        else:
            print("Well done.")

        # Ask user if they want to see their game history.
        if user_choice.lower == "xxx" or rounds_played == rounds:
            break

print()
user_history = input("Would you like to see your game history? ").lower()
if user_history == "yes" or user_history == "y":
    user_history = "yes" 
    
    rounds_won = rounds_played - rounds_lost 


# If 'yes' show game history


# Show game statistics
# **** Calculate Game Stats ******
    percent_win = (rounds_won / rounds_played) * 100
    percent_lose = (rounds_lost / rounds_played) * 100

    print()
    print("***** Game History *******")
    for game in game_summary:
        print(game)

    print()

    # displays game stats with % values to the nearest whole number
    print("******* Game Statistics *******")
    print("Win: {}, ({:.0f}%) ".format(rounds_won, percent_win))
    print("Loss: {}, ({:.0f}%) ".format(rounds_lost, percent_lose))

            

    # End of Game Statements 
    print()
    print('***** End Game Summary *****')
    print("Won: {} \t|\t List:{}".format(rounds_won, rounds_lost))

print()
print("***** Thanks for playing *****")

        
        
