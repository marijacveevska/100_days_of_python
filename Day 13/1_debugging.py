# DEBUGGING STEPS
# Describe the problem in steps
# 1. What is the for loop doing?
# 2. When is the function meant to print "you got it"
# 3. What are your assumptions about the value of the output?



def my_function():
    for i in range(1,20):
        if i == 20:
            print("you got it")
        
# The function never reaches 20 because the range function doesn't cover the end number in the backets

my_function()

