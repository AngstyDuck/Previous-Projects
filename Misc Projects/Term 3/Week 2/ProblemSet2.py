#question 3
x = input("Enter the number of minutes: ")
x = int(x)

def minutes_to_years_days(minutes):
    hours = minutes//60
    days = hours//24
    days_left = days % 365
    years = days // 365
    return (years, days_left)

years = minutes_to_years_days(x)[0]
days_left = minutes_to_years_days(x)[1]

print(str(x) + " is approximately " + str(years) + " years and " + str(days_left) + " days.")

#question 4

"""
from math import sqrt

class p1:
    x = 0
    y = 0

class p2:
    x = 0
    y = 0

class p3:
    x = 0
    y = 0

def area_of_triangle(p1,p2,p3):
    side12length = sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)
    
    side32length = sqrt((p2.x - p3.x)**2 + (p2.y - p3.y)**2)
    
    side13length = sqrt((p3.x - p1.x)**2 + (p3.y - p1.y)**2)
    
    s = (side12length + side32length + side13length)/2
    area = sqrt(s*(s-side12length)*(s-side32length)*(s-side13length))
    area = round(area,2)
    
    return area

p1.x = float(input("Enter x coordinate of the first point of a triangle: "))
p1.y = float(input("Enter y coordinate of the first point of a triangle: "))
p2.x = float(input("Enter x coordinate of the second point of a triangle: "))
p2.y = float(input("Enter y coordinate of the second point of a triangle: "))
p3.x = float(input("Enter x coordinate of the third point of a triangle: "))
p3.y = float(input("Enter y coordinate of the third point of a triangle: "))

print("The area of the triangle is " + str(area_of_triangle(p1,p2,p3)))
"""

#Question 5
"""
def compound_value_sixth_month(amt, rate):
    monthly_rate = rate / 12
    x = 0
   
    for i in range(6):
        x = (amt + x)*(1 + monthly_rate)
    
    x = round(x,2)
    return x

amt = float(input("Enter the monthly saving amount: "))
rate = float(input("Enter annual interest rate: "))

print("After the sixth month, the account value is " + str(compound_value_sixth_month(amt, rate)))
"""








