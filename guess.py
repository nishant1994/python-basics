import random

while (True):
    n1 = int(input("Input Lower Range:"))
    n2 = int(input("Input Upper Range:"))
    num = random.randint(n1, n2)
    count = 0
    while (True):
        count += 1
        guess = int(input("Guess Number:"))
        if guess > num:
            print("You guessed too high!")
        elif guess < num:
            print("You guessed too low!")
        else:
            print("You got in "+str(count)+" times")
            print("You guessed correct! Play Again.")
            break
