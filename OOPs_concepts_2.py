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

class Veichel(object):
    def __int__(self, color, fprice, speed, usetime):
        self.color = color
        self.fprice = fprice
        self.speed = speed
        self.usetime = usetime

    def getcolor(self):
        print(self.color , "is color")

    def getfprice(self):
        print(self.fprice , "is fuel price")

    def speed(self):
        print(self.speed, "is top speed")

class Car(Veichel):
    def __int__(self):
