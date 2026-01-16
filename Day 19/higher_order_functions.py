# A higher-order function is a function that either takes one or more functions as arguments or returns a function as its result

def greet(func): # higher-order function 
    return func("Hello")

def uppercase(text): # function to be passed
    return text.upper()

print(greet(uppercase))

