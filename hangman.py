    
#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

#Use a while loop to let the user guess again.
#The loop should only stop once the user has guessed all the letters in the chosen_word
#and 'display' has no more blanks ("_").Then you can tell the user they have won.

import hangman_words
import hangman_art
import random

print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

all_guessed_letter = []
display = []
for _ in range(len(chosen_word)):
    display += "_"
print(display)

lives = 6
win = 1

while win > 0: 
    guess = input("Guess a letter: ").lower()

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.

    if guess in display:
        print(f"You have guessed this letter {guess} before. Try another letter!")
        
    
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."

    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"The letter {guess} is not in the word. Try another letter!")
        lives -= 1
        if lives == 0:
            win -= 1
            print(f"You Lose! The word is {chosen_word}")

    for guessed in guess:
        all_guessed_letter += guessed
    print('Your guessed letters are ' + ",".join(all_guessed_letter))
    
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")


    if "_" not in display:
        win -= 1
        print("You Won!")

    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(hangman_art.stages[lives])

