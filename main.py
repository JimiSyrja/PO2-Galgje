name = input('What is your name?\n')
print()
print('Hi, %s.' % name)
print("Welkom to hangman")
print("Guess the country chosen to win")

#alle woorden in het spel
woorden = ["netherlands", "france", "belgium", "spain", "denmark", "finland", "luxembourg", "ukraine", "portugal"]

#hoe galg er uit moet zien
galg = [
"_________",
"|     __|__",
"|     |o o|  ",
"|     |_^_|",
"|    \\| |//",
"|      | |",
"|     // \\",
"|    //   \\",
"|",
"|_______________"  
]


#creert tijd en wat random betekent
import time
import random

#Wait 2 sec
time.sleep(2)


#kiest computer een woord
print("Type in a letter...")
woordkiezen = random.choice(woorden)
woord = (woordkiezen) 


#hoeveel beurten
turns = 10

while turns > 0:
  
  
 for char in woord:
   
  if char in guesses:

  else:
   print char  
   
    if turns == 0:
    print("helaas")
