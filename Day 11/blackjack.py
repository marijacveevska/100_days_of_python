import random

Q0 = input("Do you want to play a game of Blackjack? type 'y' or 'n': ")

if Q0 == "y":
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

    x1 = random.choice(cards)
    x2 = random.choice(cards)
    my_hand = [x1,x2]
    my_sum = sum(my_hand)

    y1 = random.choice(cards)
    y2 = random.choice(cards)
    computer_hand = [y1,y2]
    comp_sum = sum(computer_hand)
    
    print(f"Your cards: {my_hand}, current score: {my_sum}")
    

    if my_sum == 21:
        print("You got a BLACKJACK!.")
        print(f"The Computer's cards are : {computer_hand}")
        print("******* YOU WIN ******* ")
            

    elif comp_sum == 21:
        print(f"The Computer's cards are : {computer_hand}. The Computer got a BLACKJACK.! ")
        print("You Lose")

    elif my_sum > 21: 
        print("You lose. Went above 21")
        
    elif comp_sum > 21:
        print("Computer loses. Went above 21")
        print(f"The Computer's cards are : {computer_hand}")

    elif my_sum == 21 and comp_sum == 21:
        print("It is a Draw")
    
    else:
        print(f"The Computer's first card is: {computer_hand[0]}")

        def deal_cont():
            Q_deal = input("Type 'y' to get another card, type 'n' to pass: ")

            if Q_deal == "y":
                x3 = random.choice(cards)
                my_hand.append(x3)
                my_sum=sum(my_hand)

                if sum(computer_hand) >= 16:
                    computer_hand
                elif sum(computer_hand) < 16:
                    y3 = random.choice(cards)
                    computer_hand.append(y3)

                print(f"Your cards: {my_hand}, current score: {my_sum}")
        
                if my_sum > 21:
                    print("YOU LOSE!")
                    
                else:
                    deal_cont()


            elif Q_deal == "n":

                print(f"The Computer's hand is {computer_hand}, total score : {sum(computer_hand)}")    
                if sum(my_hand) <= 21 and sum(my_hand) > sum(computer_hand):
                    print("******* YOU WIN ******* ")
                    

                elif sum(my_hand) <= 21 and sum(my_hand) == sum(computer_hand):
                    print("It is a Draw")
                    

                elif sum(my_hand) <= 21 and sum(computer_hand) > 21:
                    print("******* YOU WIN ******* ")
                    

                else:
                    print("You lose")
                    
        
        deal_cont()
    
else:
    print("Good Bye")
        
