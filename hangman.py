import os
import random
import hangman_art

word_random = random.choice(hangman_art.words)

blank = []
for i in word_random :    
    blank.append('_')     
print(blank)             
end_game = False
life = 7
while not end_game :
    guess = input('Please guess one Letter of this Word :')
    count = 0
    for i in word_random :
        if i == guess :
            blank[count] = guess
            os.system('clear')
        count += 1  

    if '_' not in blank  :
        end_game = True
        print('  ****    You are Win    ****')        

    elif  life <= 0 :
        end_game = True       
        print('  ****    You are Loser    ****')
    
    if guess not in word_random :
           life -= 1
           os.system('clear')
           print(f'{hangman_art.HANGMANPICS[life]}')                          
    print(blank)
print(f'I guess the word was :  {word_random}')    

#1.Use the Word from Hangman 
#2.message to the User
#3.show Hangman
#4.if it was repeated , show message but dont lose step
#5.After each guess , delete the information in the Terminal







