from asyncore import loop
import random

# Sets rounds to 0
rounds_played = 0 

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
# Funotions go here...

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
lowest = int_check("Low Number: ")
highest = int_check("High Number: ", lowest +1)
rounds = int_check("Rounds: ", 1)

SECRET = random.randint(lowest, highest)

guess = ""

while guess != SECRET and guesses_left >= 1:

    guess = int_check("Guess: ", lowest, highest)  # replace this with integer chcker

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

        
        
