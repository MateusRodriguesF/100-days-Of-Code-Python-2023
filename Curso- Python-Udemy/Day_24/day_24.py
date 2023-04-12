# file = open("C:/Users/Mateus/Documents/Curso_Python_Udemy/Day_24/my_file.txt") # This way you  need to call the close function
# with open("C:/Users/Mateus/Documents/Curso_Python_Udemy/Day_24/my_file.txt") as file: # This way you dont need to call the close function
#     contents =  file.read()
#     print(contents)
# file.close()

with open("/new_file.txt", mode="w") as file:
    file.write("\nNew Text.")
