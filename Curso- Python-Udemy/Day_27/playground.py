# # Unlimited positional arguments ARGS
# def add(*args): 
#     num_lst = [i for i in args]
#     return sum(num_lst)
# print(add(2, 4, 6, 7, 1))

# # Kwargs Many Keyworded Arguments

# def calculate(n, **kwargs):
#     print(type(kwargs)) 
#     n += kwargs["add"]
#     n += kwargs["multiply"]
#     print(n)
# calculate(add=3, multiply=1)

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make="Nissan", model="Gt-R")
print(my_car.make)