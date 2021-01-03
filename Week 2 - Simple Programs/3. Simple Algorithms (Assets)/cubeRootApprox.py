# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 11:55:33 2016

@author: ericgrimson
"""

cube = 64
epsilon = 0.01
guess = 0.0
increment = 1
num_guesses = 0
while abs(guess**3 - cube) >= epsilon and guess <= cube:
    guess += increment
    num_guesses += 1
print('num_guesses =', num_guesses)
if abs(guess**3 - cube) >= epsilon:
    print('Failed on cube root of', cube)
else:
    print(guess, 'is close to the cube root of', cube)
