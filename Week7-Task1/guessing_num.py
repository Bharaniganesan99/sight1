##import random
##
##def guess_number():
##    secret_number = random.randint(1, 100)
##    attempts = 0
##
##    while True:
##        guess = int(input("Guess a number between 1 and 100: "))
##        attempts += 1
##
##        if guess == secret_number:
##            print(f"Congratulations! You guessed the number {secret_number} correctly.")
##            print(f"It took you {attempts} attempts.")
##            break
##        elif guess < secret_number:
##            print("Too low. Try again.")
##        else:
##            print("Too high. Try again.")
##
##guess_number()


##import random
##
##def guess_number():
##    secret_number = random.randint(1, 10)
##    attempts = 0
##
##    while True:
##        guess = int(input("Guess a number between 1 and 10: "))
##        attempts += 1
##
##        if guess == secret_number:
##            print(f"Congratulations! You guessed the number {secret_number} correctly.")
##            print(f"It took you {attempts} attempts.")
##            break
##        elif guess < secret_number:
##            print("Too low. Try again.")
##        else:
##            print("Too high. Try again.")
##
##guess_number()
##





import random
import math

lower = int(input("Enter Lower bound:- "))
upper = int(input("Enter Upper bound:- "))
 
x = random.randint(lower, upper)
print( "\n\tYou've only ",round(math.log(upper - lower + 1, 2))," chances to guess the integer!\n")

count = 0
try:
     while count < math.log(upper - lower + 1, 2):
      count += 1
 
      guess = int(input("Guess a number:- "))

      if x == guess:
        
           print("Congratulations you did it in ",count, " try")
           break

      if x > guess:
       
            print("You guessed too small!")
      if x < guess:
        
            print("You Guessed too high!")
      if count >= math.log(upper - lower + 1, 2):
            print("\nThe number is %d" % x)
            print("\tBetter Luck Next time!")

except:
    print("invalid")







##import random
##import math
##
##lower = int(input("Enter Lower bound:- "))
##upper = int(input("Enter Upper bound:- "))
## 
##x = random.randint(lower, upper)
###print( "\n\tYou've only ",round(math.log(upper - lower + 1, 2))," chances to guess the integer!\n")
##
##y = "You've only ",round(math.log(upper - lower + 1, 2)),"chances to guess the integer!"
##print(y)
##
##count = 0
##while count < y[1]:     #math.log(upper - lower + 1, 2):
##    count += 1
## 
##    guess = int(input("Guess a number:- "))
## 
##    if x == guess:
##        print("Congratulations you did it in ",
##              count, " try")
##        break
##    elif x > guess:
##        print("You guessed too small!")
##    elif x < guess:
##        print("You Guessed too high!")
## 
##if count >= y[1]:    #math.log(upper - lower + 1, 2):
##    print("\nThe number is %d" % x)
##    print("\tBetter Luck Next time!")
 

