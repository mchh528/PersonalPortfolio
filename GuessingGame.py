import random

num = random.randint(1, 100)
print(num)
count = 0;
guess = 0;

while (guess == 0):
    try:
        guess = int(input("Guess what number has the computer selected? "))
    except ValueError:
        print("Valid Answers only.")

while (num != guess):
    # If user's guess is greater than computer generated number, printing that the number guessed is too high
    while (guess > num):
        print("Too high..")
        try:
            guess = int(input("Guess what number has the computer selected? "))
            count += 1;
        except ValueError:
            print("Valid Answers only.")

    # If user's guess is less than computer generated number, printing that the number guessed is too low
    while (guess < num):
        print("Too low..")
        try:
            guess = int(input("Guess what number has the computer selected? "))
            count += 1;
        except ValueError:
            print("Valid Answers only.")
    
# If user's guess matches the computer generated number, print congratulatory message and the number of guesses it took
if (guess == num):
    count += 1;
    print("Congrats! You guessed the number! The number was {}".format(num))
    print("You took {} guesses".format(count))
