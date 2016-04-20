import random

name = raw_input("May I know your name?")
print "Hi " + name + ". We will play guess a number game. I'm thinking of a number between 1 and 20"
secretnumber = random.randint(1, 20)

# Ask the user to guess 6 times
for numberOfGuesses in range(1, 7):
    try:
        guess = int(raw_input("Take a guess"))
        if secretnumber < guess:
            print "The number I'm thinking is lower than " + str(guess) + "."
        elif secretnumber > guess:
            print "The number I'm thinking is higher than " + str(guess) + "."
        else:
            break  # Number is correct or number of guess max has reached
    except ValueError:
        print "This field accepts only numbers"
if guess == secretnumber:
    print "You guessed the number! You guessed it in " + str(numberOfGuesses) + " tries!"
else:
    print "You have failed. The correct number was " + str(secretnumber) + "."