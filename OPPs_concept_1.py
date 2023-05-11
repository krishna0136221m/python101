"""
classes
objects
constructor
destructor
"""


#
# class dog:
#     def barks(self, name):
#         self.abc = name
#         print(name, "is barking")
#
#     def eats(self, name):
#         self.name = name
#         print(name, "is eating")


# dog1 = dog()
# dog1.eats("tommy")
# dog1.barks("tommy")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def barks(self):
        print(self.name, "is barking")

    def eats(self):
        print(self.name, "is eating")

    def age(self):
        print(self.age, "year old")


dog1 = Dog("tommy", 3)
dog1.eats()


