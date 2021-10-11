################### Guess the number using the linear number steps #####################

import random

numberToGuess = random.randint(1, 10000)

guess = int(input("Guess the number: "))

while numberToGuess != guess:
    guess = int(input("Try again: "))
    
print("You guessed the number, it was:", numberToGuess)



############### Guess the number using the logarithmic number steps ########################

import random

n = 1000
numberToGuess = random.randint(1, n)

guess = int(input("Guess the number: "))

# O(log n)
while numberToGuess != guess:
    
    if numberToGuess > guess:
        print("The number is higher")
    elif numberToGuess < guess:
        print("The number is lower")
    
    guess = int(input("Try again: "))
    
print("You guessed the number, it was:", numberToGuess)



############### Computer guesses the number using the logarithmic number steps ########################

n = int(input("Enter the max number: "))
targetNumber = random.randint(1, n)
print(f"Target number: {targetNumber}")

lowerBound, upperBound, numberOfSteps = 1, n, 0

while lowerBound <= upperBound:
    numberOfSteps += 1
    guessedNumber = (lowerBound + upperBound) // 2
    
    if targetNumber < guessedNumber:
        upperBound = guessedNumber
    elif targetNumber > guessedNumber:
        lowerBound = guessedNumber
    else:
        print(f"Found the number: {guessedNumber}. Number of steps: {numberOfSteps}")
        break
    
    
