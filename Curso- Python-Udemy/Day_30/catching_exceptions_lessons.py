# # File Not Found

# try: # Try to open the file
#     file = open(r"data.txt")
#     a_dictionary = {"key":"value"}
#     print(a_dictionary["key"])

# except FileNotFoundError: # if we can't open the file
#     print("Couldn't open the file, creating a new one")
#     file = open(r"data.txt", "w") # Create a file
#     file.write("Something, here")
# except KeyError as error_message:
#     print(f"The key {error_message} doesn't exist")
# else:
#     cont = file.read()
#     print(cont)
# finally:
#     # file.close()
#     # print("File was closed successfully")
#     raise TypeError("This is a error that i made up")

# height = float(input("Height: "))
# weight = int(input("Weight: "))
# if height > 3:
#     raise ValueError("Human height should not be over 3 meters.")
# bmi = weight / height**2
# print(bmi)

# Challenge 1

# fruits = ["Apple", "Pear", "Orange"]
# #TODO: Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit Pie")
#     else:
#         print(fruit + " pie")
# make_pie(4)
# Challenge 2
# facebook_posts = [
#     {'Likes': 21, 'Comments': 2}, 
#     {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
#     {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
#     {'Comments': 4, 'Shares': 2}, 
#     {'Comments': 1, 'Shares': 1}, 
#     {'Likes': 19, 'Comments': 3}
# ]
# total_likes = 0
# for post in facebook_posts:
#     try:
#         total_likes = total_likes + post['Likes']
#     except KeyError:
#         pass
#         total_likes += 0
# print(total_likes)
