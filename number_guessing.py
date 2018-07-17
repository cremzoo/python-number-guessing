#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 18:38:15 2018

@author: cremz1
"""

import random

guesses = []

myComputer = random.randint(1, 70)

player = int(input("Enter a number between 1-70:"))
guesses.append(player)

while player != myComputer:
    if player > myComputer:
        print("Number is too high!")
    else:
        print("Number is too low!")
    player = int(input("Enter a number between 1-70: "))
    guesses.append(player)

else:
    print("You have guessed right! Good job!")
    print("It took you %i guesses. " % len(guesses))
    print("This were your guesses:")
    print(guesses)
