import random

yes_no = input('do you want to play a game ')
while yes_no == 'yes':

    n = random.randint(1, 10)
    while int(input("guess the number: ")) != n:
        print("Try again")
    print("Congrats, you guessed")

    yes_no = input('do you want to play a game ')