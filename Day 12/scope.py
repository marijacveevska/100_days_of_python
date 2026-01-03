# Definition : The scope of a variable refers to the context in which that variable is visible/accessible to the Python interpreter.

enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


# Local Scope : 
def drink_potion1():
    potion_strength = 3
    print(potion_strength)


drink_potion1()
# print(potion_strength) # NameError: name 'potion_strength' is not defined



# Global Scope
player_health = 10

def drink_potion2():
    potion_strength = 3
    # player_health+=1. # UnboundLocalError: cannot access local variable 'player_health' where it is not associated with a value
    player_health_upgrade = player_health+potion_strength

    print(potion_strength)
    print(player_health)
    print(player_health_upgrade)

drink_potion2()

