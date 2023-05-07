"""
this program is for leap year
if year is divisible by 400 leap year
if year is divisible by 4 and not by 100 then leap year
"""
print("enter year", end=" ")
year = int(input())
if year % 400 == 0:
    print("year is leap year")
elif year % 4 == 0 and year % 100 != 0:
    print("year is leap year")
else:
    print("year is not leap year")
