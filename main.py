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
# made by globalsilver#9994
print(Colorate.Vertical(Colors.blue_to_purple, intro, 1))
infront = input("What do u want to be in front of the generated strings:")
amount = int(input('Amount of strings to generate: '))
lenght = int(input('string lenght:'))
letters= input("Letters?(y/n)>")
clear()
if letters == "y":
 print ("select what type of letters you want to be in the string")
 print ("Both      >1")
 print ("Lowercase >2")
 print ("Uppercase >3")
 cases = int(input(">"))
if letters == "y":
 lol = input("numbers? [y/n]\n>")
optimized = input("coloured text?[y/n](might be slower)\n>") 
value = 1
startTime = time.time()

if letters == "n":
 cases = 0
 lol = "lol"

if lol == "y" and cases < 2:
  while value <= amount:
   code = infront + ('').join(
   random.choices(string.ascii_letters + string.digits, k=lenght ))
   f = open('Strings.txt', "a+")
   f.write(f'{code}\n')
   f.close()
   if optimized == "y":
    print(Colorate.Horizontal(Colors.purple_to_red,(f'[GENERATED] {code}')))
   else:
    print (f'[GENERATED] {code}')
   value += 1
   system(f'title {value}/{amount}')
   
   

if lol == "y" and cases < 3:
  while value <= amount:
   code = infront + ('').join(
   random.choices(string.ascii_lowercase + string.digits, k=lenght ))
   f = open('Strings.txt', "a+")
   f.write(f'{code}\n')
   f.close()
   if optimized == "y":
    print(Colorate.Horizontal(Colors.purple_to_red,(f'[GENERATED] {code}')))
   else:
    print (f'[GENERATED] {code}')
   value += 1
   system(f'title {value}/{amount}')

if lol == "y" and cases < 4:
  while value <= amount:
   code = infront + ('').join(
   random.choices(string.ascii_uppercase + string.digits , k=lenght ))
   f = open('Strings.txt', "a+")
   f.write(f'{code}\n')
   f.close()
   if optimized == "y":
    print(Colorate.Horizontal(Colors.purple_to_red,(f'[GENERATED] {code}')))
   else:
    print (f'[GENERATED] {code}')
   value += 1
   system(f'title {value}/{amount}')
   
if lol == "n" and cases < 2:
  while value <= amount:
   code = infront + ('').join(
   random.choices(string.ascii_letters, k=lenght ))
   f = open('Strings.txt', "a+")
   f.write(f'{code}\n')
   f.close()
   if optimized == "y":
    print(Colorate.Horizontal(Colors.purple_to_red,(f'[GENERATED] {code}')))
   else:
    print (f'[GENERATED] {code}')
   value += 1
   system(f'title {value}/{amount}')
   
if lol == "n" and cases < 3:
  while value <= amount:
   code = infront + ('').join(
   random.choices(string.ascii_lowercase, k=lenght ))
   f = open('Strings.txt', "a+")
   f.write(f'{code}\n')
   f.close()
   if optimized == "y":
    print(Colorate.Horizontal(Colors.purple_to_red,(f'[GENERATED] {code}')))
   else:
    print (f'[GENERATED] {code}')
   value += 1
   system(f'title {value}/{amount}')

if lol == "n" and cases < 4:
  while value <= amount:
   code = infront + ('').join(
   random.choices(string.ascii_uppercase, k=lenght ))
   f = open('Strings.txt', "a+")
   f.write(f'{code}\n')
   f.close()
   if optimized == "y":
    print(Colorate.Horizontal(Colors.purple_to_red,(f'[GENERATED] {code}')))
   else:
    print (f'[GENERATED] {code}')
   value += 1
   system(f'title {value}/{amount}')

if letters == "n":
  while value <= amount:
   code = infront + ('').join(
   random.choices(string.digits, k=lenght ))
   f = open('Strings.txt', "a+")
   f.write(f'{code}\n')
   f.close()
   if optimized == "y":
    print(Colorate.Horizontal(Colors.purple_to_red,(f'[GENERATED] {code}')))
   else:
    print (f'[GENERATED] {code}')
   value += 1
   system(f'title {value}/{amount}')


print(Colorate.Color(Colors.green, "Done", True))
executionTime = (time.time() - startTime)
print('It took ' + str(round(executionTime, 2)) + ' seconds to generate '+ str(amount) + ' strings')
