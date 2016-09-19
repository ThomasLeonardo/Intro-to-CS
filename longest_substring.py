# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

result = ""
length = 0
lastLetter = 'a'
current = ""
count = 0

s = 'abcdefghijklmnopqrstuvwxyz'

for letter in s:
    if(ord(lastLetter) <= ord(letter)):
        count+= 1
        current += letter
    else:
        if(count > length):
            length = count
            result = current
        count = 1
        current = letter
    lastLetter = letter
if(count > length):
    result = current
print("Longest substring in alphabetical order is:",result)