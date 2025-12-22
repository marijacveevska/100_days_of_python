import random

friends = ["Marija", "Petar", "Nate", "Jana", "Max", "Petar_T"]
generated_number = random.randint(0,5)

chosen_friend = friends[generated_number]

print(chosen_friend)
print(generated_number)

# Option 2

chosen_friend_method = random.choice(friends)
print(chosen_friend_method)