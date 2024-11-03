# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 22:33:25 2024

@author: soeze
"""

import random #importing random library for the random quiz

def displayMenu(): #creating function for the menu
    print("DIFFICULTY LEVEL")
    print(" 1. Easy")
    print(" 2. Moderate")
    print(" 3. Advanced")
    return int(input("Select a difficulty level (1-3): "))

def randomInt(difficulty): #creating function to generate random number 
    if difficulty == 1: #easy mode
        return random.randint(1, 9)
    elif difficulty == 2: #medium mode
        return random.randint(10, 99)
    elif difficulty == 3:#hard mode
        return random.randint(1000, 9999)

def decideOperation():#creating function for the random operation
    return random.choice(['+', '-'])

def displayProblem(num1, num2, operation):#Creating function for the display operation
    if operation == '+':
        correct_answer = num1 + num2
    else:
        correct_answer = num1 - num2

    print(f"{num1} {operation} {num2} = ")
    return int(input()), correct_answer

def isCorrect(user_answer, correct_answer):#creating function for the checking answers
    return user_answer == correct_answer

def displayResults(score):#creating function for the score
    print(f"Your final score is: {score} out of 100")
    if score > 90:
        print("Rank: A+")
    elif score > 80:
        print("Rank: A")
    elif score > 70:
        print("Rank: B")
    elif score > 60:
        print("Rank: C")
    else:
        print("Rank: D")

def main():#Running the program
    while True:
        difficulty = displayMenu()
        score = 0

        for _ in range(10):
            num1 = randomInt(difficulty)
            num2 = randomInt(difficulty)
            operation = decideOperation()

            user_answer, correct_answer = displayProblem(num1, num2, operation)

            if isCorrect(user_answer, correct_answer):
                score += 10
                print("Correct!")
            else:
                print("Incorrect, try again!")
                user_answer, _ = displayProblem(num1, num2, operation)
                if isCorrect(user_answer, correct_answer):
                    score += 5
                    print("Correct!")
                else:
                    print(f"Wrong again. The correct answer was {correct_answer}")

        displayResults(score) #Display the result

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    main()
