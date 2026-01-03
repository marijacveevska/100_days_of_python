import random

dice_letters = ["a","b","c","d","e","f"]
dice_num = random.randint(1,6)
print(dice_num)
print(dice_letters[dice_num])

# Lists start from 0 so this list we have a randint range 0 - 5 so when 6 comes in the dice_num it gives IndexError: list index out of range