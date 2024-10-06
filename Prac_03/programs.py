# 1. Tax

"""
TAX_RATE_LOW = 0.05
TAX_RATE_HIGH = 0.1
TAX_THRESHOLD_LOW = 100
TAX_THRESHOLD_HIGH = 1000
total_tax = 0

get income

if income >= TAX_THRESHOLD_LOW && income <= TAX_THRESHOLD_HIGH:
    total_tax = income * TAX_RATE_LOW
else if income > TAX_THRESHOLD_HIGH:
    total_tax = income * TAX_RATE_HIGH

take_home_pay = income - total_tax

display "Total Tax", total_tax
display "Take home pay", take_home_pay
"""

TAX_RATE_LOW = 0.02
TAX_RATE_MID = 0.05
TAX_RATE_HIGH = 0.1
TAX_THRESHOLD_LOW = 100
TAX_THRESHOLD_MID = 500
TAX_THRESHOLD_HIGH = 1000
total_tax = 0

print("Python Party Tax Program - Where Tax is a Party")
income = float(input("Income: $"))

if income >= TAX_THRESHOLD_LOW and income <= TAX_THRESHOLD_MID:
    total_tax = income * TAX_RATE_LOW
elif income > TAX_THRESHOLD_MID and income <= TAX_THRESHOLD_HIGH:
    total_tax = income * TAX_RATE_MID
elif income > TAX_THRESHOLD_HIGH:
    total_tax = income * TAX_RATE_HIGH

take_home_pay = income - total_tax

print("Total Tax is: $", total_tax)
print("Take home pay is: $", take_home_pay)


# 2. Car Insurance

"""
insurance_condition = "Hire refused"

get age

if age >= 18 and age <25
    insurance_condition = "Insurance required"
else if age >= 25:
    insurance_condition = "Insurance not required"
display "Insurance condition", insurance_condition
"""
insurance_condition = "Hire refused"

age = int(input("Enter age: "))

if age >= 18 and age <25:
    insurance_condition = "Insurance required"
elif age >= 25:
    insurance_condition = "Insurance not required"

print("Insurance Condition:", insurance_condition)

# test case:
# input         Output
# 10,17         Hire refused
# 18,19,24      Insurance required
# 25, 28        Insurance not required



# 3. Simple Password Checker
"""
SECRET_PASSWORD = "tryme"

get password

if password == SECRET_PASSWORD:
    display "Access Granted"
else:
    display "Access Denied"
"""

SECRET_PASSWORD = "tryme"

password = input("Enter your password: ")

if password == SECRET_PASSWORD:
    print("Access Granted")
else:
    print("Access Denied")


# 4. Basketball

"""
get shots
get shots_made

shooting_percentage = (shots_made/shots) * 100

display "Number of shots attempted: ", shots
display "Number of shots made: ", shots_made
display "Shooting Percentage", shooting_percentage

if shooting_percentage >= 50
    display "That's great!" 
"""

shots = int(input("Number of shots attempted: "))
shots_made = int(input("Number of shots made: "))

shooting_percentage = (shots_made/shots) * 100

print("Number of shots attempted: ", shots)
print("Number of shots made: ", shots_made)
print(f"Shooting Percentage {shooting_percentage:.1f}%" )

if shooting_percentage >= 50:
    print("That's great!")




#5 Rock of Ages
"""
get age
if age >= 0 and age <= 120
    if age < 13
        display "Kid"
    else if age >= 13 and age <= 19
        display "Teen"
    else if age >= 20 and age <= 35
        display "Young"
    else if age >= 36 and age <= 60
        display "Prime life"
    else:
        display "Elderly"
else
    display "Invalid Age"

"""

age = int(input("Enter age: "))

if age >= 0 and age <= 120:
    if age < 13:
        print("Kid")
    elif age >= 13 and age <= 19:
        print("Teen")
    elif age >= 20 and age <= 35:
        print("Young")
    elif age >= 36 and age <= 60:
        print("Prime life")
    else:
        print("Elderly")
else:
    print("Invalid Age")




# 6. Speeding Fines
"""

MINOR_SPEEDING_FINE = 309
MODERATE_SPEEDING_FINE = 464
SIGNIFICANT_SPEEDING_FINE = 696
SEVERE_SPEEDING_FINE = 1161
EXCESSIVE_SPEEDING_FINE = 1780

get speed
get speed_limit

speed_over_limit = speed - speed_limit

if speed_over_limit < 11
    fine = MINOR_SPEEDING_FINE
else if speed_over_limit >= 11 and speed_over_limit <= 20
    fine = MODERATE_SPEEDING_FINE
else if speed_over_limit >= 21 and speed_over_limit <= 30
    fine = SIGNIFICANT_SPEEDING_FINE
else if speed_over_limit >= 31 and speed_over_limit <= 40
    fine = SEVERE_SPEEDING_FINE
else if speed_over_limit > 40
    fine = EXCESSIVE_SPEEDING_FINE
else
    fine = 0

display "Fine for speeding $", fine
"""

MINOR_SPEEDING_FINE = 309
MODERATE_SPEEDING_FINE = 464
SIGNIFICANT_SPEEDING_FINE = 696
SEVERE_SPEEDING_FINE = 1161
EXCESSIVE_SPEEDING_FINE = 1780

speed = float(input("Enter the speed (km/h): "))

speed_limit = float(input("Enter the speed limit (km/h): "))

speed_over_limit = speed - speed_limit

if speed_over_limit <= 0:
    fine = 0
elif speed_over_limit > 0 and speed_over_limit < 11:
    fine = MINOR_SPEEDING_FINE
elif speed_over_limit >= 11 and speed_over_limit <= 20:
    fine = MODERATE_SPEEDING_FINE
elif speed_over_limit >= 21 and speed_over_limit <= 30:
    fine = SIGNIFICANT_SPEEDING_FINE
elif speed_over_limit >= 31 and speed_over_limit <= 40:
    fine = SEVERE_SPEEDING_FINE
else:
    fine = EXCESSIVE_SPEEDING_FINE

print(f"Fine for speeding is ${fine}")