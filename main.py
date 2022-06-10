import time
import random
name = input('What is your name?\n')
print () #Leeg
print('Hi, %s.' % name)
print("Welkom to hangman")
print("Guess the country chosen to win")
print() #Leeg

woorden = ["netherlands", "france", "belgium", "spain", "denmark", "finland", "luxembourg", "ukraine",
"portugal","hungary","china","india","nepal","russia","brazil","norway","poland"]

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
#Checkt hoeveel kansen je nog hebt
while turns > 0:         

    #begin bij 0
    letters_not_guesed = 0             
    toonwoord=''

    #voor ieder letter in het woord
    for char in woord:      

    #kijk of de letter in het woord zit
        if char in guesses:    
    
        #laat het letter zien
            toonwoord=toonwoord + (char)    

        else:
    
        #als het karakter er niet in zit, zet een streepje
            toonwoord=toonwoord + ('_')     
       
        #aantal keer mis + 1
            letters_not_guesed += 1    

    print ('Word:',toonwoord, '. Already picked letters:', guesses)
    print () #Leeg

    
    #Toont "je hebt gewonnen scherm"
    if letters_not_guesed == 0:
        print () #Leeg
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

    #laat het aantal keer gegokt zien 
    guesses += guess                    

    #als letter niet in het woord zit
    if guess not in woord:  
 
     #1 leven er af
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
        print () #Leeg
 
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

