import random
 
name = input("What is your name? ")
print("Good Luck ! ", name)
 
given_words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
print(given_words)
 
word = random.choice(given_words)
 
 
print("Guess the characters")
 
guesses = ''
turns = 5
 
 
while turns > 0:
 
    failed = 0
 
    for char in word:
 
        if char in guesses:
            print(char, end=" ")
 
        else:
            print("_")
 
            failed += 1
 
    if failed == 0:
    
        print("You Win")
 
       
        print("The word is: ", word)
        break
 
    print()
    guess = input("guess a character:")
 
  
    guesses += guess
 

    if guess not in word:
 
        turns -= 1
 
       
        print("Wrong")
 
        print("You have", + turns, 'more guesses')
 
        if turns == 0:
            print("You Loose")
