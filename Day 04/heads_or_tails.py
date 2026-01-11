import random

input("what do you choose: heads or tails? ")

rand_num = random.randint(0,1)

if rand_num == 1:
    print("heads")
elif rand_num == 0:
    print("tails")
else:
    print("not valid")


