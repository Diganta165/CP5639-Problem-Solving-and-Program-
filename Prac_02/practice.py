# BMI

"""
get height
get weight
bmi = weight / (height ** 2)
display bmi
"""

# height = float(input("Enter your height in meter:"))
# weight = float(input("Enter your weight in kilograms: "))
# bmi = weight / (height ** 2)
# print("BMI:", bmi)


# Maths Operators
"""
get lhs
get rhs
display lhs + rhs
display lhs - rhs
display lhs * rhs
display lhs / rhs
display lhs // rhs
display lhs ** rhs
"""

# lhs = float(input("Enter left had side number: "))
# rhs =  float(input("Enter right had side number: "))
#
# print(f"{lhs} + {rhs} is {lhs  + rhs}")
# print(f"{lhs} - {rhs} is {lhs - rhs}")
# print(f"{lhs} * {rhs} is {lhs * rhs}")
# print(f"{lhs} / {rhs} is {lhs / rhs}")
# print(f"{lhs} // {rhs} is {lhs // rhs}")
# print(f"{lhs} ** {rhs} is {lhs ** rhs}")

# Number Conversions
"""
KG_IN_POUNDS = 2.20462
FEET_IN_METERS = 0.3048

display options of conversion (1 to convert kilograms to pounds, 2. convert pounds to kilograms, 3. convert fahrenheit to celsius, 4. convert celsius to fahrenheit, 5. feet to meters, 6. meters to feet)
get option

if option == 1
    get value_kg
    
    display value_kg in pounds value_kg * KG_IN_POUNDS 
else if option == 2
    get value_pounds
    display value_pounds in kilograms  value_pounds / KG_IN_POUNDS
else if option == 3
    get value_fahrenheit
    display value_fahrenheit in celsius (value_fahrenheit - 32) * (5/9)
else if option == 4
    get value_celsius
    display value_celsius in fahrenheit  (value_celsius * (9/5)) + 32
else if option == 5
    get value_feet
    display value_feet in meters  value_feet * FEET_IN_METERS
else if option == 6
    get value_meter
    display value_meter in feet value_neter / FEET_IN_METERS
else display Invalid Option
"""
# KG_IN_POUNDS = 2.20462
# FEET_IN_METERS = 0.3048
#
# option = int(input("Choose option to make a conversion: \n1.kilograms to pounds \n2.pounds to kilograms \n3.fahrenheit to celsius \n4. celsius to fahrenheit \n5.feet to meters \n6.meters to feet \n Enter your value here:"))
#
# if option == 1:
#     value_kg = float(input("Enter value in kilograms: "))
#     print(f"{value_kg} kg in pound is {value_kg * KG_IN_POUNDS}")
# elif option == 2:
#     value_pounds = float(input("Enter value in pounds: "))
#     print(f"{value_pounds} pounds in kilogram is {value_pounds / KG_IN_POUNDS}")
# elif option == 3:
#     value_fahrenheit = float(input("Enter value in fahrenheit: "))
#     print(f"{value_fahrenheit} fahrenheit in celsius is {(value_fahrenheit - 32) * (5/9)}")
# elif option == 4:
#     value_celsius = float(input("Enter value in celsius: "))
#     print(f"{value_celsius} celsius in fahrenheit is {(value_celsius * (9/5)) + 32}" )
# elif option == 5:
#     value_feet = float(input("Enter value in feet: "))
#     print(f"{value_feet} feet in meter is {value_feet * FEET_IN_METERS} meters")
# elif option == 6:
#     value_meter = float(input("Enter value in meters: "))
#     print(f"{value_meter} meter in feet is {value_meter / FEET_IN_METERS} feet")
# else:
#     print("Invalid Option")