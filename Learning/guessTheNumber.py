import random

name = raw_input("May I know your name?")
print "Hi " + name + ". We will play guess a number game. I'm thinking of a number between 1 and 20"
number = random.randint(1, 20)
print "DEBUG: " + "Secret number is: " + str(number)
for numberOfGuesses in range(1, 7):
    guess = int(raw_input("Take a guess"))
    if guess > number:
        print "The number is lower than " + str(guess) + "."
    elif guess < number:
        print "The number is higher than " + str(guess) + "."
    else:
        break  # Number is correct or number of guess max has reached
if guess == number:
    print "You guessed the number! You guessed it in " + str(numberOfGuesses) + " tries!"
else:
    print "You have failed. The correct number was " + str(number) + "."