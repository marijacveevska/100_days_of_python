import random
from higher_lower_art import art
from game_data import data

print(art)

current = random.choice(data)

still_play = True
score = 0
while still_play:

    
    challenger = random.choice(data)
    while challenger == current :
        challenger = random.choice(data)

    
    A_name = current['name']
    A_description = current['description']
    A_country = current['country']
    A_followers = current['follower_count']
    #print(A_followers)
    print(f"A: {A_name}, {A_description} from {A_country}")

    B_name = challenger['name']
    B_description = challenger['description']
    B_country = challenger['country']
    B_followers = challenger['follower_count']
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
        current = challenger
        print(f"You're right! Current score: {score} \n")
    else:
        still_play = False
        print(f"\nSorry, that's wrong. Your score is {score}\n")
