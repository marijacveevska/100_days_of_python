''' write a function called calculate_love_score() that tests the compatibility between two names.  To work out the love score between two people: 
1. Take both people's names and check for the number of times the letters in the word TRUE occurs.   
2. Then check for the number of times the letters in the word LOVE occurs.   
3. Then combine these numbers to make a 2 digit number and print it out. 
e.g.
name1 = "Angela Yu" name2 = "Jack Bauer"
T occurs 0 times 
R occurs 1 time 
U occurs 2 times 
E occurs 2 times 
Total = 5 

L occurs 1 time 
O occurs 0 times 
V occurs 0 times 
E occurs 2 times 
Total = 3 

Love Score = 53
'''

def calculate_love_score(name1,name2):
    names = (name1+name2).lower()
    names_list = list(names)

    print(names_list)

    T = 0
    R = 0
    U = 0
    E = 0

    for elem in names_list:
        if elem=="t" in names_list:
            T +=1
        elif elem=="r" in names_list:
            R +=1
        elif elem=="u" in names_list:
            U +=1
        elif elem=="e" in names_list:
            E +=1

    print(f"T occurs {T} times")
    print(f"R occurs {R} times")
    print(f"U occurs {U} times")
    print(f"E occurs {E} times")

    Total_true= T+R+U+E
    print(f"Total = {Total_true}")

    L = 0
    O = 0
    V = 0
    E = 0

    for elem in names_list:
        if elem=="l" in names_list:
            L +=1
        elif elem=="o" in names_list:
            O +=1
        elif elem=="v" in names_list:
            V +=1
        elif elem=="e" in names_list:
            E +=1

    print(f"L occurs {L} times")
    print(f"O occurs {O} times")
    print(f"V occurs {V} times")
    print(f"E occurs {E} times")

    Total_love= L+O+V+E
    print(f"Total = {Total_love}")

    total_true = str(Total_true)
    total_love = str(Total_love)

    print(f"Love Score = {total_true + total_love}")

calculate_love_score("Kanye West","Kim Kardashian")

