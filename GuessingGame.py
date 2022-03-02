import random

highest = 1000
answer = random.randint(1, highest)
print("Please guess a number between 1 and {}: ".format(highest))
guess = int(input())

guesses = 0

#if guess != answer:
if guess == answer:
    print("You guessed correct the first time")
elif guess == 0:
    print("Game over")
else:
    while guess != answer:
        if guess > answer:
            print("Please guess lower")
        elif guess == 0:
            print("Game over")
        else:
            print("please guess higher")
        guesses += 1
        guess = int(input())
    print("You guessed correct!")
