import time
import random

print("Welcome!")
time.sleep(1)
print("This is a simple number guessing program.")
time.sleep(1)
num = random.randint(0, 100)

guess = int(input("Enter a number between 0 and 100"))
count = 0

while guess != num:

    if guess > num:
        print("Your number is too high")
        count += 1
        time.sleep(2)
        guess = int(input("Enter a number between 0 and 100"))
    elif guess < num:
        print("Your number is too low")
        count += 1
        time.sleep(2)
        guess = int(input("Enter a number between 0 and 100"))

if guess == num:
    print("Congratulations! You have guessed the correct number!")
    print("It took you " + str(count) + " guesses")






