class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathing(self):
        print( "Inhale, exhale.")


class Fish(Animal):# creating a Fish subclass that inherits from the Animal class
    def __init__(self):
        super().__init__()#this line should be called to initialize the class Animal 

    def breathing(self):#changing the breathing method
        super().breathing()
        print("Doing this uhnderwater.")

    def swim(self):
        print("Moving in water.")


nemo = Fish()
nemo.swim()
nemo.breathing()