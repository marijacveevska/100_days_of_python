# Global variables should be avoided except when we have GLOBAL CONSTANTS

# In this example here with the enemies, instead of making enemies "Global" inside the function, you can just pass it as an input
enemies = 1

def increase_enemies(enemy):
    print(f"previous enemies: {enemies}")
    return enemy + 1

enemies = increase_enemies(enemies)
print(f"current enemies: {enemies}")


# GLOBAL CONSTANTS are variables that you know will never change and always need to be written in CAPS LOCK

PI = 3.14159
GOOGLE_URL = "https://www.google.com"
