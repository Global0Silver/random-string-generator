import pystyle
import time
from pystyle import Colors, Colorate
import random, string
import os
from os import system
clear = lambda: os.system('cls')
clear()
intro =  """
  ▄████  ██▓     ▒█████   ▄▄▄▄    ▄▄▄       ██▓         ██████  ██▓ ██▓  ██▒   █▓▓█████  ██▀███  
 ██▒ ▀█▒▓██▒    ▒██▒  ██▒▓█████▄ ▒████▄    ▓██▒       ▒██    ▒ ▓██▒▓██▒ ▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
▒██░▄▄▄░▒██░    ▒██░  ██▒▒██▒ ▄██▒██  ▀█▄  ▒██░       ░ ▓██▄   ▒██▒▒██░  ▓██  █▒░▒███   ▓██ ░▄█ ▒
░▓█  ██▓▒██░    ▒██   ██░▒██░█▀  ░██▄▄▄▄██ ▒██░         ▒   ██▒░██░▒██░   ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
░▒▓███▀▒░██████▒░ ████▓▒░░▓█  ▀█▓ ▓█   ▓██▒░██████▒   ▒██████▒▒░██░░██████▒▒▀█░  ░▒████▒░██▓ ▒██▒
 ░▒   ▒ ░ ▒░▓  ░░ ▒░▒░▒░ ░▒▓███▀▒ ▒▒   ▓▒█░░ ▒░▓  ░   ▒ ▒▓▒ ▒ ░░▓  ░ ▒░▓  ░░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
  ░   ░ ░ ░ ▒  ░  ░ ▒ ▒░ ▒░▒   ░   ▒   ▒▒ ░░ ░ ▒  ░   ░ ░▒  ░ ░ ▒ ░░ ░ ▒  ░░ ░░   ░ ░  ░  ░▒ ░ ▒░
░ ░   ░   ░ ░   ░ ░ ░ ▒   ░    ░   ░   ▒     ░ ░      ░  ░  ░   ▒ ░  ░ ░     ░░     ░     ░░   ░ 
      ░     ░  ░    ░ ░   ░            ░  ░    ░  ░         ░   ░      ░  ░   ░     ░  ░   ░     
                               ░                                             ░                   
"""
print(Colorate.Vertical(Colors.blue_to_purple, intro, 1))
infront = input("Enter a string to be put before the generated text:")
#input loops to check if a valid number has been entered
while True:
 amount = input('Amount of strings to generate: ')
 if amount.isnumeric() == True:
  break
 else:
  print ("Please enter a valid number")
while True:
    lenght = input('string lenght:')
    if lenght.isnumeric() == True:
     break
    else:
     print ("Please enter a valid number")

  
clear()
#cases system
print ("select what type of letters you want to be in the string (leave blank for no letters")
print ("Both      >1")
print ("Lowercase >2")
print ("Uppercase >3")
cases = input(">")
if cases == "1":
 prnt_cases = string.ascii_letters
elif cases == "2":
 prnt_cases = string.ascii_lowercase
elif cases == "3":
 prnt_cases = string.ascii_uppercase
else:
 prnt_cases = string.digits # if none selected generate numbers instead
 
#number system
inp_numbers = input("numbers? [y/n]\n>")
if inp_numbers == "y":
 prnt_numbers = string.digits
else:
 prnt_numbers = ""
 
colorfull = input("coloured text?[y/n](might be slower but cooler)\n>") 
value = 1
startTime = time.time()
f = open('Strings.txt', "a+") #opens the txt file

while value <= int(amount): # main part
   code = infront + ('').join(
   random.choices(prnt_cases + prnt_numbers, k=int(lenght) ))
   f.write(f'{code}\n')
   if colorfull == "y":
    print(Colorate.Horizontal(Colors.purple_to_red,(f'[GENERATED] {code}')))
   else:
    print (f'[GENERATED] {code}')
   print (str(value) + "/" + amount ,end = "\r")
   value += 1 

print(Colorate.Color(Colors.green, "\nDone", True))
executionTime = (time.time() - startTime)
print('It took ' + str(round(executionTime, 2)) + ' seconds to generate '+ str(amount) + ' strings')
f.close()#exits out of the txt file