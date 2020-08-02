# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 16:19:27 2019

@author: petru
"""

numbers = [34, 45, 71, 82, 34, 56, 12, 24] #variabila cu lista de numere
for numb in numbers: #loop through the list and store each item into the variable numb 
    if numb >= 23: #conditia 'if' daca in numb sunt nr. mai mari decat "xx" 
        print(numb) #atunci print numerele ramase dupa 'if' 
#dupa for se pot face alte operatii 
print("end")
alte = [34, 45, 71, 82, 34, 56, 12, 24]
alte.append(8) #folosim comanda apppend
for this in alte:
    if this % 2 == 0: #acest cod '% 2 == 0' este valabil pentru 'if the number is even,'
        print(this) #print it out, va printa numerele even
        