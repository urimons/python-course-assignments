import random

random_number = random.randint(1, 20)
guess = int(input("Please guess a number between 1 to 20:"))
if guess < random_number:
    print ("Your chosen number is too low!")
elif guess > random_number:
    print("Your chosen number is too high!")
else:
    print("Correct answer! What are the chances?!")
