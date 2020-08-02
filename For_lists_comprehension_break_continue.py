# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 14:51:50 2020

@author: petru
"""

drink_choices = ["coffee", "tea", "water", "juice", "soda"]

num = [1, 2, 5, 7, 9, 8, 13, 3, 6, 11, 22]

drink = ["coffee", "tea", "water", "juice", "soda"]

for drink in drink_choices:
  print(drink)
  
#daca vrei sa creezi o lista incepand cu numere negative 
lists = [i - 5 for i in range(10)]
print(lists)
# functia break se va opri din iterat si va afisa pina la numarul cu care se imparte egal
for i in num:
    if i % 2 == 0:
      print("Stop")
      break
    print(i)
#functia continue afiseaza numerele care au rest    
for i in num:
    if i % 2 == 0:
      continue
    print(i)

choices = [i for i in drink if i != 'water']  
print(choices)


caramida = []
for i in drink:
    if i == "water":
        caramida += drink[i]
    print(caramida)

