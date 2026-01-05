"""
Work in progress
"""
import random
from higher_lower_art import art
from game_data import data

print(art)



still_play = True
score = 0
while still_play:

    x = random.randint(0,49)
    y = random.randint(0,49)
    if y == x :
        if y == 0:
            y += 1
        else:
            y -=1

    
    A_name = data[x]['name']
    A_description = data[x]['description']
    A_country = data[x]['country']
    A_followers = data[x]['follower_count']
    #print(A_followers)
    print(f"A: {A_name}, {A_description} from {A_country}")

    B_name = data[y]['name']
    B_description = data[y]['description']
    B_country = data[y]['country']
    B_followers = data[y]['follower_count']
    #print(B_followers)
    print(f"B: {B_name}, {B_description} from {B_country}")

    guess = input("Who has more followers? Type A or B : ").lower()
    
    def check_answer(A_follow,B_follow,guess):
        if guess == "a" and A_follow > B_follow:
            return True
        elif guess == "b" and B_follow > A_follow:
            return True
        else:
            
            return False
            
    is_correct = check_answer(A_followers,B_followers,guess)
    if is_correct == True:
        score +=1
        print(f"You're right! Current score: {score} \n")
    else:
        still_play = False
        print(f"Sorry, that's wrong. Your score is {score}")
