# Super() function (as in super for superclass) = function used in child class to call methods from a parent class(superclass).
#                                                 Allows you to extend the functionality of the inherited methods.

#takes care of whatever attributes all the types of shapes have in common, 

class Shape():
    def __init__(self, colour, is_filled):
        self.colour = colour
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.colour} and {'filled' if self.is_filled else 'not filled'}")


class Circle(Shape):
    def __init__(self, colour, is_filled, radius):
        super().__init__(colour, is_filled)
        self.radius = radius

    # If a child has the same method as parent, childs method will be executed instead aka method overwriting
    def describe(self):
        print(f"It is pi")
        # Use this to call the parents function as well
        super().describe()

class Square(Shape):
    def __init__(self, colour, is_filled, width):
        super().__init__(colour, is_filled)
        self.width = width

class Triangle(Shape):
    def __init__(self, colour, is_filled, width, height):
        super().__init__(colour, is_filled)
        self.width = width
        self.height = height

circle = Circle(colour="Red", is_filled=True, radius=5)
square = Square(colour="blue", is_filled=False, width=6)

print(square.colour)
print(square.is_filled)
print(square.width)

circle.describe()



































# # # Multiple inheritance = inherit from more thn one parent class
# #                          C(A, B)

# # Multilevel inheritance = inherit from a parent which inherits from another parent
# #                          C(B)  <- B(A)  <- A

# class Animal():

#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print(f"{self.name} is eating")

#     def sleep(self):
#         print(f"{self.name} is sleeping")

# class Prey(Animal):
#     def flee(self):
#         print(f"{self.name} is fleeing")

# class Predator(Animal):
#     def hunt(self):
#         print(f"{self.name} is hunting")

# class Rabbit(Prey):
#     pass

# class Hawk(Predator):
#     pass

# class Fish(Prey, Predator):
#     pass

# rabbit = Rabbit("Bugs")
# hawk = Hawk("Tony")
# fish = Fish("Nemo")

# fish.eat()





















# # Inheritance = allows a class to inherit attributes and methods from other classes to help with code reusability

# class Animal():

#     def __init__(self, name):
#         self.name = name
#         self.is_alive = True

#     def eat(self):
#         print(f"{self.name} is eating.")

# class Dog(Animal):
#     def speak(self):
#         print("Woof!")

# class Cat(Animal):
#     pass

# dog = Dog("Harold")
# cat = Cat("Barney")

# print(dog.name)
# print(cat.name)
# cat.eat()
# dog.eat()
# dog.speak()