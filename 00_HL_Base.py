import random 

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


GUESSES_ALLOWED = 5

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
            print("Too low, try a higher number. Guesses left:")

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



