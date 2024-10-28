"""
CP1401 2024 TR3 Assignment 1
Program 3 – Hiking Tracker
Student Name: Md Shafiur Rahman Diganta
Date started: 28 / 10 / 2024
Pseudocode:

LOWEST_DAY_DISTANCE_THRESHOLD = 0
HIGHEST_DAY_DISTANCE_THRESHOLD = 120
distance = 0

display "Hiking Tracker"
get days

while days <= 0
    display "Invalid number of days"
    get days

count = 0
while count < days
    get day_distance

    while LOWEST_DAY_DISTANCE_THRESHOLD < 0 or HIGHEST_DAY_DISTANCE_THRESHOLD > 120
        display "invalid distance"
        get day_distance

    distance += day_distance
    count += 1


display "total distance" distance
display "average distance" distance/days km

if day_distance > distance/days
    final_day_performance = "above"
else if day_distance < distance/days
    final_day_performance = "below"
else if day_distance == distance/days
    final_day_performance = "the same as your"

display "display On your final day, your distance was {final_day_performance} average."


"""

LOWEST_DAY_DISTANCE_THRESHOLD = 0
HIGHEST_DAY_DISTANCE_THRESHOLD = 120
distance = 0

print("Hiking Tracker")
days = int(input("Enter number of days: "))

while days <= 0:
    print("Invalid number of days")
    days = int(input("Enter number of days: "))

count = 0
while count < days:
    day_distance= float(input(f"Day {count+1} distance:"))

    while day_distance < LOWEST_DAY_DISTANCE_THRESHOLD or day_distance > HIGHEST_DAY_DISTANCE_THRESHOLD:
        print("invalid number of days")
        day_distance = float(input(f"Day {count+1} distance:"))

    distance += day_distance
    count += 1


print(f"\nYour total distance was: {distance}km")
print(f"Your average distance was: {distance/days}km")

if day_distance > distance/days:
    final_day_performance = "above"
elif day_distance < distance/days:
    final_day_performance = "below"
elif day_distance == distance/days:
    final_day_performance = "the same as your"

print(f"display On your final day, your distance was {final_day_performance} average.")
