# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 15:55:35 2019

@author: petru
"""

#or loops are traditionally used when you have a block 
#of code which you want to repeat a fixed number of times
#Having an iterable method basically means that the data can be presented in list form
#iterate a repeta
for x in range(0, 3):
    print("We're on time %d" % (x))
    
for i in range(1, 100):
    print(i)
    
print('Is it greater', 5 > 2)
print('Hens do eggs', 20.0/6.0)
print(type(20 / 6))
cars = 90 
my_name = 'Petru'
my_age = 36 
my_weight = 70
my_height = 183
print('There are',cars, 'cars in parking area')
print('My name is %s and i have %s old.' % (my_name, my_age))
print('I have my name %s and %s old %s height.' % (my_name, my_age, my_height))
#eroare de genul 'TypeError: %d format: a number is required, not str' nu accepta mai multe numere trebuie
#sa folosesti %s formatters sau %r, %d do not work with one string si mai mute int
#We use %r for debugging, since it displays the “raw” data of the variable, but we use %s and
#others for displaying to users.
joke_evaluation = "Isn't that joke funny? %r" #fara formatter la final de propozitie va afisa eroare 
hilarious = 'False'
print(joke_evaluation % hilarious)
print("Isn't that joke funny?", hilarious, '.')
print("." * 10)# interesant afiseaza 10 puncte 

end1 = 'P'
end2 = 'E'
end3 = 'T'
end4 = 'R'
end5 = 'U'
print(end1 + end2 + end3 + end4 + end5)
formatter = "%r %r %r %r" # formatter %r 
print(formatter % (1, 2, 3, 4))
print(formatter % ('cat', 'dog', 'cow', 'andr'))
print(formatter % ('u', 'i', 'd', 'r'))#nu poate afisa un cuvant fara pauza intre litere nu este ca si concanate
# invalid sysntax, comma missing after true print(formatter % ( True False, True, False))
print(formatter % ( True, False, True, False))# boolean operators 
# You should use %s and only use %r for getting debugging(inspection) information about something.
# debugging = the process of identifying and removing errors from computer hardware or software.
months = "Jan\nNov\nJan\nFeb\nMar"# va afisa lunile de la November in forma de array 
#\n newlines put a new line character into the string at that point, the \ (backslash) desparte caracterele si le muta cun rand mai jos 
print("here are the months", months)
print(""" 
      There is no love without pain
      There is no rose without thorne
      There is chance without hope""")
print("")
print("\t There're birds into the three \v and other things like bugs and \n insects.")
#Escaping characters '\' backlash to display in a tring the quoutes is placed in front of single double quote
#Escaping \f elimina din editor inainte de escaping operator
#Escaping \r elimina primul rand din string 
#Input intersting joculet cu input() function care is assigned(alocata) la o variabila dupa care printam valoare variabilei 
#in consola de output vor aparea intrebarile la care userul va trebui sa raspunda iar la urma automat in ultima 
#propozitie va afisa informatia din raspunsurile tale 
print("How old are you?",)
age = input()
print("How much do weight?",)
weight = input()
print("how tall are you?",)
height = input()

print("So, you are %r and weight %r and tall %r." % (age, weight, height))
#Notice that we put a , (comma) at the end of each print line. This is so that
#print doesn’t end the line with a new line character and go to the next line.

#un alt exemplu 
age = input("How old are you")
print( "So you are %r old" % (age))
#Remember, %r is for debugging and is “raw representation” while %s is for display.

