import random
import my_module_randomness

random_num = random.randint(1,10)
print(random_num)
print(my_module_randomness.my_favorite_number)
sum_num = float(random_num) + my_module_randomness.my_favorite_number

print(sum_num)

# random distributions

random_num1 = random.random()         # this gives any random float between 0 and 1
random_num2 = random.random() * 10    # this gives any random float between 0 and 10

random_uniform = random.uniform(1,10)

print(random_num1, random_num2, random_uniform)