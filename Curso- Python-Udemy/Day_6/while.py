# Reborg Challenge  https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def move_goal():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
# i = 6
# while i > 0:
#     move_goal()
#     i -= 1

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def move_goal():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
# while not at_goal():
#     move_goal()


# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def gira():
#         turn_left()
#         move()
#         turn_right()
#         move()
#         turn_right()
#         move()
#         if wall_in_front:
#             turn_left()
# while not at_goal():
#     if wall_in_front():
#         gira()
#     else:
#         move()

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def gira():
#         turn_left()
#         while wall_on_right():
#             move()
#         turn_right()
#         move()
#         turn_right()
#         move()
#         while front_is_clear():
#             move()
#         if wall_in_front:
#             turn_left()

# while not at_goal():
#     if wall_in_front():
#         gira()
#     else:
#         move()

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()