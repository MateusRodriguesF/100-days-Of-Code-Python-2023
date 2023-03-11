programing_dictionary = {"bug":"An error in a program that prevents the program from running as expected.", "function":"A piece of code that you can easily call over and over again."}

# print(programing_dictionary["bug"])

# print(programing_dictionary["function"])

# Adding new items to the dictionary

# programing_dictionary["Loop"] = "A new item"

# wiping an existing dictionary

# programing_dictionary = {}

#  Editing an item in the dictionary

# programing_dictionary["bug"] = "An error in a program."

# Loop trough a  dictionary
# for key, value in programing_dictionary.items():
#     print(key)
#     print(value)

# for key in programing_dictionary:
#     print(programing_dictionary[key])


# Day 9 Challenge

# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }

#TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}

# for key in student_scores:
#     note = student_scores[key]
#     if note > 90 and note <= 100:
#         student_grades[key] = "Outstanding"
#     elif note > 80 and note <= 90:
#         student_grades[key] = "Exceeds Expectations"
#     elif note > 70 and note <= 80:
#         student_grades[key] = "Acceptable"
#     else:
#         student_grades[key] = "Fail"

# print(student_grades)

# Nesting 

# capitals = {
#     "France" : "Paris",
#     "Germany" : "Berlin",
#     "Spain" : "Madrid",
#     "Italy" : "Rome"
# }

#Nesting a list in a dictionary 

# travel_log = {
#     "France" : ["Paris", "Berlin", "Madrid", "Rome"],
#     "Germany" : ["Berlin", "Madrid", "Rome"],
# }

# Nesting a dictionary inside a dictionary

# travel_logss = {
#     "France" : {"cities_visited" : ["Paris", "Berlin", "Madrid", "Rome"], "total_visits" : 12},
#     "Germany" : {"cities_visited" : ["Berlin", "Madrid", "Rome"], "total_visits" : 15}
# }

# Nesting a dictionary inside a list

# travel_logs = [
#     {
#     "country": "France",
#     "cities_visited": ["Paris", "Berlin", "Madrid", "Rome"],
#     "total_visits": 12
#     },
#     {
#     "country": "Germany",
#     "cities_visited": ["Berlin", "Madrid", "Rome"],
#     "total_visits": 15
#     }
# ]

#  Day 9 Challenge 

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

#to be added to the travel_log. 👇
def add_new_country(country_visited, times_visited, cities_visited):
    
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)
    
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# for values in travel_log:
#     print(values)
for values in travel_log:
    cidades = list(values["cities"])
    print(cidades[2])

# print(travel_log[0]["cities"][1])


