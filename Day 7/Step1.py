import random

word_list = ["spaceman","camel","cartoon","triangle"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it

chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-4 - Create an empty string called placeholder where you put _ for each letter in the chosen word.

placeholder = "_" * len(chosen_word)

print(placeholder)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("Guess a letter \n").lower()
print(guess)

# TODO-3 - Check if the letter the user guessed is one of the letters in the chosen_word. Print "right" or "wrong" depending if is correct or not


if guess in chosen_word:
    print("Right")
else:
    print("Wrong")


# TODO-5 - Create a "display" that puts the guessed letter in the right place in the placeholder.

display=""
for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"

print(display)