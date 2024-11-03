# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 22:10:33 2024

@author: soeze
"""

import random #importing library for the random joke

def load_jokes(filename): #Creating function to load jokes from the file
    jokes = []
    with open(filename, 'r') as file:
        for line in file:
            setup, punchline = line.strip().split('?')
            jokes.append((setup + '?', punchline))
    return jokes

def tell_joke(jokes): #Creating function to tell jokes from the file
    joke = random.choice(jokes)
    setup, punchline = joke
    print(setup)
    input("Press any key to see the punchline...")
    print(punchline)

def main(): #Running the program multiple time until user quit
    jokes = load_jokes("randomJokes.txt")
    while True:
        user_input = input("Type 'Alexa tell me a Joke' or 'quit' to exit: ").lower()
        if user_input == "quit":
            break
        elif user_input == "alexa tell me a joke":
            tell_joke(jokes)
        else:
            print("Invalid input. Try again.")

if __name__ == "__main__":
    main()
