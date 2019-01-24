"""
Hangman.

Authors: Alyssa Taylor, Kaitlin Weik, and Hannah Meisner.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

# TODO: 2. Implement Hangman using your Iterative Enhancement Plan.

####### Do NOT attempt this assignment before class! #######

import random


def main():

    correct = ''

    #Welcome
    print('HELLO!!')
    name = str(input('Whats your name: '))
    length = int(input('Enter MAXIMUM length for secret word:'))
    for k in range(length):
        correct = correct + '_'

    tries = int(input('How many guesses do you want?'))
    triesLeft = tries
    word = random_word(length)

    while triesLeft > 0:
        triesLeft = checker(guess(), word, triesLeft)

    if triesLeft == 0:
        print(word)


def random_word(length):
    with open('words.txt') as f:
        f.readline()
        string = f.read()
        words = string.split()

        while True:
            word = words[random.randrange(0, len(words))]
            if len(word) <= length:
                break

    return word


def guess():
    letter = str(input('Enter your guess:'))
    return letter


def checker(letter, word, triesLeft, correct):
    if letter in word:
        print('Guess Correct! You have', triesLeft, 'guess(es) remaining.')
        for k in range(len(word)):
            correct = 
    else:
        triesLeft = triesLeft - 1
        print('Incorrect! You have', triesLeft, 'guess(es) remaining.')

    return triesLeft


def known(word, correct):




main()