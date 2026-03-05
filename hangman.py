import os
import random
import hangman_art

word_random = random.choice(hangman_art.words)

blank = []
for i in word_random :    
    blank.append('_')     
print(blank)             
end_game = False
life = -1
hang_open = False
guessed = []

while not end_game :
    guess = input('Please guess one Letter of this Word :')   
    count = 0
    for i in word_random :
        if i == guess :
            blank[count] = guess
            os.system('clear')
        count += 1  

    if guess in guessed :
        os.system('clear')
        print ('you have already guess this letter')
    elif guess not in word_random :
        life += 1
        os.system('clear')
        hang_open = True
        
    guessed.append(guess)
    if  hang_open : 
        print(f'{hangman_art.HANGMANPICS[life]}')   

    blank_str = ''
    for i in blank:
        blank_str += i 
    print(blank_str)

    if '_' not in blank  :
        end_game = True
        print('  ****    You are Win    ****')        

    elif  life >= 6 :
        end_game = True       
        print('  ****    You are Loser    ****')
    
print(f'choice words was :  {word_random}')    

#1.Use the Word from Hangman 
#2.message to the User
#3.show Hangman
#4.if it was repeated , show message but dont lose step
#5.After each guess , delete the information in the Terminal
