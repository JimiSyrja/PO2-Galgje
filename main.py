import time
import random
name = input('What is your name?\n')
print ()
print('Hi, %s.' % name)
print("Welkom to hangman")
print("Guess the country chosen to win")
print()

woorden = ["netherlands", "france", "belgium", "spain", "denmark", "finland", "luxembourg", "ukraine", "portugal","hungary","china","india","nepal","russia"]

galg = [
"_________       ",
"|     __|__     ",
"|     |o o|     ",
"|     |_^_|     ",
"|     \| |/   ",
"|      | |      ",
"|      / \     ",
"|     /   \    ",
"|               ",
"|_______________"  
]

#Wait 2 sec
time.sleep(2)

print("Type in a letter...")
woordkiezen = random.choice(woorden)
woord = (woordkiezen)

guesses = ''

#je krijgt 10 kansen
turns = 10

#maakt een loop
#Kijkt hoeveel keer nog
while turns > 0:         

    #begin bij 0
    letters_not_guesed = 0             
    toonwoord=''

    #voor ieder karacter in het woord
    for char in woord:      

    #kijk of het karakter in het woord zit
        if char in guesses:    
    
        #laat het karakter zien
            toonwoord=toonwoord + (char)    

        else:
    
        #als het karakter er niet in zit, zet een streepje
            toonwoord=toonwoord + ('_')     
       
        #aantal keer mis + 1
            letters_not_guesed += 1    

    print ('Word:',toonwoord, '. Already picked letters:', guesses)
    print () # emtpy line

    #als fail is gelijk aan 0
    #Je hebt gewonnen
    if letters_not_guesed == 0:
        print ()
        print ('...')
        #wait for 1 second
        time.sleep(1)        
        print ('Congrats,', name, 'you win!!!')

    # exit
        break              

    print

    #raad een letter
    #wait for 1 second
    time.sleep(1)   
    guess = input ('Guess a letter: ') 

    #zet het aantal keer gokken 
    guesses += guess                    

    #als het niet is gevonden in het woord
    if guess not in woord:  
 
     #Er gaat er steeds 1 af
        turns -= 1        

        # teken galg
        galgregel=turns
        nr_of_to_print_lines=(10-turns)
        while nr_of_to_print_lines>0:
          print (galg[galgregel])
          galgregel +=1 
          nr_of_to_print_lines -=1
        print ("")

    # print fout
        print ('Incorrect ...')
        print ()
 
    #hoeveel keer nog
        print (name, 'You have', + turns, 'turns') 

    #zet aantal keer naar 0
        if turns == 0:           
    
        # print je hebt verloren, 
            print ()
            print ('...')
            #wait for 1 second
            time.sleep(1)   
            print ('Too bad', name, 'you lost, the country was:', woord)
