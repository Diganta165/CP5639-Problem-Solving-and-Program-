"""
CP1401 2024 TR3 Assignment 1
Program 1 – Pizza Pay Calculator
Student Name: Md Shafiur Rahman Diganta
Date started: 28 / 10 / 2024
Pseudocode:

PAY_PER_TRIP = 1.45
PAY_PER_MINUTE = 0.95

get trips, minutes

trip_payment = trips * PAY_PER_TRIP
minute_payment = minutes * PAY_PER_MINUTE


display trip_payment
display minute_payment

display trip_payment + minute_payment
"""

PAY_PER_TRIP = 1.45
PAY_PER_MINUTE = 0.95

print("Warm Pizza Pay Calculator ")
trips = int(input("Number of trips: "))
minutes = int(input("Number of minutes: "))

trip_payment = trips * PAY_PER_TRIP
minute_payment = minutes * PAY_PER_MINUTE


print(f"For {trips} trips, your pay is: ${trip_payment}")
print(f"For {minutes} minutes, your pay is: ${minute_payment}")
print(f"Your total pay is ${trip_payment + minute_payment:,.2f}")
