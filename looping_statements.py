# add number between some range
"""
add = 0
print("enter number", end=" ")
a = int(input())
print("decide the range", end=" ")
b = int(input())
for i in range(a, b - 1):
    add = add + i
print(add)
"""

# print number for 10 to 0
"""
for i in range (10,0,-1):
    print(i)
"""

# program to print even number between some range
# first method
"""
print("enter starting range number", end=" ")
a = int(input())
print("enter last range number", end=" ")
b = int(input())
print("even number between ", a, " is ", b)
for i in range(a, b - 1):
    if (i % 2 == 0):
        print(i, end=" ")
"""
"""
#second method
for i in range(1,11,2):
     print(i,end=" ")
"""

# WAP to print multiplication of table
"""
print("enter number for table")
num = int(input())
for i in range(1, 11):
    print(num, " x ", i, " = ", num * i)
"""

# WAP to print patter
"""
print("enter no of rows")
rows=int(input())
for i in range(0,rows):
    for j in range(1,i+1):
        print("*",end="")
    print("\n")
"""
# 2nd way
"""
for i in range(0, 6):
    for j in range(0, 6):
        if j <= i:
            print("*", end="")
    print("")
"""

# WAP to print pattern in reverse order
"""
for i in range(0, 6):
    for j in range(0, 6):
        if (j >= 6 - i):
            print("*", end="")
        else:
            print(" ", end="")
    print("")
"""

# WAP to print equi-traingular pattern
"""
for i in range(0, 4):
    for j in range(0, 7):
        if 3-i <=j <= 3+i:
            print("*", end="")
        else:
            print(" ", end="")
    print("")
"""

# while loop
"""
WAP to print no form 1 to 10
i = 0
while i <= 10:
    print(i)
    i += 1
"""


"""
WAP to print no for 10 to 1
i=10
while i>=0:
    print(i)
    i-=1
"""