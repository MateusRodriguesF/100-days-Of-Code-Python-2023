## ********Day 54 Start**********
## Functions can have inputs/functionality/output
# def add(n1, n2):
#     return n1 + n2

# def subtract(n1, n2):
#     return n1 - n2

# def multiply(n1, n2):
#     return n1 * n2

# def divide(n1, n2):
#     return n1 / n2

#Functions are first-class objects, can be passed around as arguments e.g. int/string/float etc.

# def calculate(calc_function, n1, n2):
#     return calc_function(n1, n2)


# result = calculate(add, 2, 3)
# print(result)


#Functions can be nested in other functions
#Functions can be returned from other functions

# def outer_function():
#     print("Im Outer!")

#     def nested_function():
#         print("Im inner!")

#     return nested_function   #without the parentesis to avoid call the nested function itself

# inner_function = outer_function() #calls only the outer function
# inner_function() #calls also the nested function

#Python Decrator function
import time
def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        #Do something before you run the function
        function()
        #Do something after you run the function
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello")

@delay_decorator
def say_bye():
    print("Bye")

@delay_decorator
def greetings():
    print("how are you?")


say_hello()