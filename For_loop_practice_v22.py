# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 10:26:05 2019

@author: petru
"""

hobbies = []

# Add your code below!
#for loop in range(3):
  #hobby = input("hobby: ")
  #hobbies.append(str(hobby))#daca schimbam continutul din paranteze cu un integer rasp va fi diferit 
#incearca sa schimbi continutul din append cu un inteher sau un string""
  #print(hobbies)
  

word = "Marble"
for char in word:
   print(char, )
   
phrase = "A bird in the hand..."

# Add your for loop
for char in phrase:
  if char == "A" or char == "a":
    print("X",)
  else:
    print(char,)
    
    
    
    
d = {'x': 9, 'y': 10, 'z': 20}
for key in d:
    print(key, "9", "10", "20")
    
  #if d[key] == 10:
    #print "This dictionary has the value 10!"

choices = ['pizza', 'pasta', 'salad', 'nachos']
print("Your choice are")

for index, item in enumerate(choices):
    print(index + 1, item)
   
print()
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]
#a, b sunt elemente in listele list_a and b 
for a, b in zip(list_a, list_b):
    if list_a > list_b:
        print(max(a, b))    
        
print()
#check out the indentation, else is executed after for but only if for ends normally that 
#is not with break function if hits tomatto else block will  not be executed 
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

for f in fruits:
   if f == 'tomato':
        print('This is not fruit') 
   print('A', f)
else:
    print("A fine selection of fruits")






    
    