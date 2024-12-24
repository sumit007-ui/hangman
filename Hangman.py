import random
from hangman_words import Word_list
from hangman_art import stages

logo = r''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

print(logo)
lives = 6

chosen_word = random.choice(Word_list)
print(chosen_word)

Placeholder = ""
Word_lenght = len(chosen_word)
for position in range ((Word_lenght)):
    Placeholder += "_"
game_over = False 
correct_letter = []    

while not game_over:
    guess = input("Guess a letter: ").lower()
        
    print(guess)

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"

    print(display)


    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You Lose!")

    if "_"  not in display:
            game_over = True
            print("You Win!")

    print(stages[lives])


