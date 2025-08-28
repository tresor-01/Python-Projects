import random

print("Hello Welcome to the NUmber Guessing Game")
name = str(input("Please enter the name you will be using:"))

print("Choose the number ")
print("******************")

playernum = int(input("Please enter the number between 1 and 10:"))
time  = int(input("enter the number of time you will be playing "))

computer_num = random.randrange(1,10)

for i in range( time):
  if playernum == computer_num :
    print(name," you guessed the right number")
    exit
  else:
   print( name,"lost the numbers don't match")
   playernum = int(input("Please enter the number between 1 and 100:"))