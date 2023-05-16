"""
polymorphism
>>overloading
>operator overloading
>function overloading
>>overriding

inheritance
s
"""


# operator overloading -> when different /same  operators have different implementations depending on their arguments.
# print(2+3)
# print("cse"+ " ccml")


# function overloading -> when a function have same name  but different parameters
# print(len([1,3,6]))
# print(len("krishna"))
# print(len((1,3)))
# print(len({
#     "name":"krishna",
#     "profession":"learning"
# }))




#inheritance

# class Person(object):
#     def __init__(self , fname , lname):
#         self.firstname=fname
#         self.lastname=lname
#
#     def name(self):
#         print(self.firstname , self.lastname)
#
#
# class Students(Person):
#     def __init__(self,fname, lname):
#         Person.__init__(self,fname,lname)
#
#     def years(self,year):
#         print("year is",year)
#
#
# s1=Students("krishna", "yadav")
# s1.name()
# s1.years(2023)

"""
types of inheritance
->single inheritance
->multiple inheritance
->multilevel inheritance
->herarical inheritance
->hybrid inheriance
"""

# overiding
#
# class Person(object):
#     def __init__(self , fname , lname):
#         self.firstname=fname
#         self.lastname=lname
#
#     def name(self):
#         print(self.firstname , self.lastname)
#
#
# class Students(Person):
#     def __init__(self,fname, lname):
#         self.fname=fname
#         self.lname=lname
#         Person.__init__(self,fname,lname)
#
#     # here name method is overriding(person-students)
#     def name(self):
#         print("Name of student : ",self.fname + " " + self.lname)
#     def years(self,year):
#         print("year is",year)
#
# s1= Students("Ram" , "singh")
# s1.name()




#dunder method in python

#some other type of variable > class variable > instance variable
# @classmethod
# @staticmethod

# class Person():
#     # class variable or static vaiable -> which intialize outside __init__ / instance and it is bound to class
#     var="class variable"
#     var2="class method"
#     def name(self,name):
#         # instance variable -> which is intailized inside the instance and it is bounded to instance
#         self.name=name
#         print(name )
#         #acessing class variable
#         print(self.var)
#
#     @classmethod     # these are bounded to class
#     def vardata(cls):
#         print(cls.var2)
#
#     @staticmethod   # these are not bounded to class or instances
#     def printhello():
#         print("hello world")
#
# print(Person.var)
# p1=Person()
# p1.name("krishna")
#
# #modification in class variable
# Person.var="class variable modified"
# print(Person.var)
# #calling class method -> it cannot be acess by objects
# Person.vardata()
# Person.printhello()


# abstraction
# from abc import ABC , abstractmethod
#
# class shape(ABC):
#     @abstractmethod
#     def calculate_area(self):
#         pass
#
#
# class traingle(shape):
#     def __init__(self, base , height):
#         self.base = base
#         self.height=height
#     def calculate_area(self):
#         area=(self.base*self.height)/2
#         print(area)
#
# t1=traingle(3,6)
# t1.calculate_area()
