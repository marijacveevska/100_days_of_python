# Defined input variables

def add(n1,n2):
    return n1 + n2

print(add(3,5))


# Unlimited [Positional] Arguments

def print_numbers(*args):
    for n in args:
        print(n)


print_numbers(3,5,7,9)

def add(*args):
    sum = 0
    for n in args:
        sum +=n
    return sum
        

print(add(2,3,4))

# Unlimited Keyword Arguments

def example_kwargs(**kwargs):
    print(kwargs) # print the dictionary


    for key,value in kwargs.items():  # loop through the key value pairs
        print(key)
        print(value)

    print(kwargs["add"])  # print the value for this key


example_kwargs(add=3,multiply=5)    

def calculate(n,**kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2,add=3,multiply=5)    


# CLASS with kwards

class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw.get("model") # if you don't want to specify model, use .get() function so it will return NONE instead of error 
        

my_car1 = Car(make="Nissan",model="GT-R")
print(my_car1)
print(my_car1.model)
my_car2 = Car(make="Toyota")
print(my_car2.model)