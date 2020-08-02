# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 19:20:30 2019

@author: petru
"""

i = 1 
while i > 6:
    print(i)
    i += 1
else:
    print("m-am prins")

from random import randint

print("Lucky Numbers! 3 numbers will be generated.")
print("If one of them is a '5', you lose!")

count = 0 
while count < 3:
    num = randint(1, 6)
    print(num)
    if num == 5:
        print("Sorry you lose")
        break
    count += 1
else:
    print("You win")
        
#un alt exemplu de joculet 
random_number = randint(1, 10) # nu inteleg cum programul ia acest random!!!!  
i = 3
while i > 0:
 guess = int(input(" Please try: "))
 if guess == 3: 
    print("you win")
    break
 i -= 1
else:
    print("You lose")



    