

import random 

number=random.randint(1,9)
#for testing that random number is coming or not 
#print(number)
chance = 0 

print(' Welcome to my game . ')
print('Guess a number between (1 to 9 )')
guess= input('Enter your Guess :-')

if guess == number :
   print('Yay ! You did it you won ')


if not chance < 5 :
  ('You loose . The number is ' , number)


   
while chance < 5 :
  chance=chance+1