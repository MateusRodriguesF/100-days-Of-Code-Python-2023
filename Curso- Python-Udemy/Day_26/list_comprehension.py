# Challenge 1
# You are going to write a List Comprehension to create a new list called squared_numbers. This new list should contain every number in the list numbers but each number should be squared.

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above 👆
# #Write your 1 line code 👇 below:
# squared_numbers = [n *n for n in numbers]
# #Write your code 👆 above:
# print(squared_numbers)


# Challenge 2 
# You are going to write a List Comprehension to create a new list called result. This new list should only contain the even numbers from the list numbers.

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above
# #Write your 1 line code 👇 below:
# result = [n for n in numbers if n % 2 == 0]
# #Write your code 👆 above:
# print(result)

# Challenge 3
# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.
# You are going to create a list called result which contains the numbers that are common in both files.

# with open("file1.txt") as file1:
#     file_1_data = file1.readlines()
# with open("file2.txt") as file2:
#     file_2_data = file2.readlines()
# result = [int(num) for num in file_1_data if num in file_2_data] # List Comprehension
# # Write your code above 👆
# print(result)

# Dictionary Comprehension 👇
# import random
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# students_scores = {student:random.randint(1,100) for student in names}
# print(students_scores)
# passed_students = {student:score for (student,score) in students_scores.items() if score >= 60}
# print(passed_students)

# Challenge 4 

# You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the given sentence and calculates the number of letters in each word.

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆
# # Write your code below:
# result = {word:len(word) for word in sentence.split()}
# print(result)

# Challenge 5

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# # 🚨 Don't change code above 👆

# # Write your code 👇 below:
# weather_f = {day:nv * 9/5+32 for (day, nv) in weather_c.items()}
# print(weather_f)

# How to iterate over a pandas DataFrame
import pandas as pd

students_dict = {
    "student": ["Angela", "James", "John"],
    "scores": [56, 76, 98]
}
student_data_frame = pd.DataFrame(students_dict)
# print(student_data_frame)

for (index, row) in student_data_frame.iterrows():
    print(row.scores)
 