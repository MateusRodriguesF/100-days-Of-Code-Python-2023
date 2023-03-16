from replit import clear
clear()
# print("#" * 10, "scopes", "#" * 10)
# enemies = 1
# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")
# increase_enemies()
# print(f"enemies outside function: {enemies}")

# print("#" * 10, "Local Scopes", "#" * 10)

# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)

# drink_potion()
# #print(potion_strength)#error

#global scope

# player_health = 10 #Global v

# def drink_potion():
#     potion_strength = 2
#     print(player_health)

# There is no Block Scope

# game_level = 3
# enemies = ["Skeleton", "Zombie", "Alien"]
# if game_level < 5:
#     new_enemie = enemies[0]

# print(new_enemie)


# Modifying Global Scope

enemies = 1

def increase_enemies():
    # global enemies : dont use to change variables
    print(f"enemies inside function: {enemies}")
    return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")


# Global constants

PI = 3.14159 # constants should have be in Upper Case 

