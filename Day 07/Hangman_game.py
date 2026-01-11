import random
from hangman_words import word_list

# Step 1
# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it
# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# TODO-3 - Check if the letter the user guessed is one of the letters in the chosen_word. Print "right" or "wrong" depending if is correct or not
# Step 2
# TODO-4 - Create an empty string called placeholder where you put _ for each letter in the chosen word.
# TODO-5 - Create a "display" that puts the guessed letter in the right place in the placeholder.
# Step 3
# TODO-6 - Use a while loop to let the user guess again and the loop whould stop only when the user has guessed all the letters in the chosen_word. At this point the display has no more blanks
# TODO-7 - Change the for loop so that you keep the previous correct guesses
# Step 4
# TODO-8 - Create a variable called lives to keep track of the of the number of lives left
# TODO-9 - If guess is not a letter in the chosen_word then reduce lives by 1. If lives goes to 0 then game_over = True and print "You Lose!"
# TODO-10 - print the stages that correspond to the current number of lives the user has remaining


stages=["x_x",":'(",":(",":|",":O",":)",":D"]


chosen_word = random.choice(word_list)


placeholder = "_" * len(chosen_word)

print(f"{placeholder} \n")


game_over = False

correct_letters = []
guessed_letters = set()

lives = 6

while not game_over:
    guess = input("Guess a letter:  ").lower()

    if guess in guessed_letters:
        print("You already said this letter\n")
        continue

    guessed_letters.add(guess)

    display=""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
            
        elif letter in correct_letters:
            display+= letter

        else:
            display += "_" 

    print(f"{display} \n")


    if guess not in chosen_word:
        lives -= 1
        print("Wrong")
        print(f"Lives left: {lives}")
    else:
        print("Correct")

    print(f"{stages[lives]} \n")

    if "_" not in display:
        game_over = True
        print("************** You win! **************")

    if lives == 0:
        game_over = True
        print("************** You Lose! **************")
        print(f"The chosen word is: {chosen_word} \n") 


