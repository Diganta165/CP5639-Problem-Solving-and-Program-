# 1. Discount Price
"""
get original_price
discount = original_price * 0.2
new_price = original_price – discount
print new_price
"""

FIXED_DISCOUNT = 0.2
original_price = float(input("Enter the original price: $"))
discount = original_price * FIXED_DISCOUNT
new_price = original_price - discount
print("New Price: $", new_price)

# 2. Kilometers to Miles
"""
ONE_KM_IN_MILES = 0.621371
get distance_km
distance_miles = distance_km * ONE_KM_IN_MILES
display distance_miles
"""
ONE_KM_IN_MILES = 0.621371

distance_km = float(input("Enter distance in kilometers:"))
distance_miles = distance_km * ONE_KM_IN_MILES
print(f"Distance in miles: {distance_miles} miles")


#3 Holiday Cost
"""
HOTEL_COST_PER_DAY = 75
get daily_food_cost
get daily_activity_cost
get trip_days

total_trip_cost = (daily_food_cost * trip_days) + (daily_activity_cost * trip_days) + (HOTEL_COST_PER_DAY * trip_days)
display total_trip_cost 

"""
HOTEL_COST_PER_DAY = 75
daily_food_cost = float(input("Daily food cost: $"))
daily_activity_cost = float(input("Daily activity cost: $"))
trip_days = int(input("Number of trip days: "))
total_trip_cost = (daily_food_cost * trip_days) + (daily_activity_cost * trip_days) + (HOTEL_COST_PER_DAY * trip_days)

print(f"The trip will cost ${total_trip_cost}")


# 4. Deep Sleep Calculation
"""
get total_sleep_seconds
get deep_sleep_seconds

deep_sleep_percentage = (deep_sleep_seconds * 100) / total_sleep_seconds
deep_sleep_minute = deep_sleep_seconds // 60
deep_sleep_seconds

display deep_sleep(in minute)
display total_sleep(in minute)
display deep_sleep_percentage
"""

sleep_time_seconds = int(input("Total sleep in seconds: "))
deep_sleep_time_seconds = int(input("Deep sleep in seconds: "))

deep_sleep_percentage = (deep_sleep_time_seconds * 100) / sleep_time_seconds
total_deep_sleep_minutes = deep_sleep_time_seconds // 60
total_deep_sleep_seconds = deep_sleep_time_seconds % 60

total_sleep_minutes = sleep_time_seconds // 60
total_sleep_seconds = sleep_time_seconds % 60

print(f"Deep Sleep : {total_deep_sleep_minutes}m {total_deep_sleep_seconds}s")
print(f"Total Sleep : {total_sleep_minutes}m {total_sleep_seconds}s")
print("Deep Sleep Percentage :", deep_sleep_percentage)