#This is a Guess the Number game.
import random

guessesTaken = 0
randRange1 = 1
randRange2 = 20
turnRange = 6

print('Hello! What is your name?')
myName = input() 

number = random.randint(randRange1, randRange2)
print('Well, ' + myName + ", I am thinking of a number between %s and %s." % (randRange1, randRange2))

for guessesTaken in range(turnRange):
    print('Take a guess.')
    try:
        guess = int(input())                    
        if guess < number:
            print('Your guess is too low.')

        if guess > number:
            print('Your guess is too high.')

        if guess == number:
            break
    except ValueError:
        print('Whoops! That guess isn\'t valid.')
        continue

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    if guessesTaken != 1:
        print('Good job, ' + myName + '! You guessed my number in ' + str(guessesTaken) + ' guesses!')
    else:
        print('Good job, ' + myName + '! You guessed my number in ' + str(guessesTaken) + ' guess!') 

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number + '.')