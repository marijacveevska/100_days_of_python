# Prime Number Checker
# Prime numbers are numbers that can only be cleanly divided by themselves and 1. 

# You need to write a function called is_prime() that checks whether if the number passed into it is a prime number or not.  It should return True or False.

import math

def is_prime(num):
    if num <= 1:
        print("Not prime")

    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            print("Not prime") 
            return
    else:
        print("Prime")



is_prime(365)