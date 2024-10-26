# 1. Percentage Change
"""
get original_value
get change_value

result = original_value + (original_value * change_value)

display original_value, change_value, result
"""

# original_value = float(input("Enter Original Value: "))
# change_value = float(input("Enter Change Value: "))
#
# result = original_value + (original_value * change_value)
#
# print(f"Original Value: {original_value}, Change Value: {change_value}, Result: {result}")

# 2. Time of day

"""
get time
get movement

if time < 12
    time_message = before
else
    time_message = after


if movement == coming
    movement_message = coming. Hi
else
    movement_message = going. Bye
    
display time_message, movement_message

"""

# time = int(input("Time: "))
# movement = input("Movement: ").lower()
#
# if time < 12:
#     time_message = "before"
# else:
#     time_message = "after"
#
# if movement == "coming":
#     movement_message = "coming. Hi"
# else:
#     movement_message = "going. Bye"
#
# print(f"It is {time_message} noon and you are {movement_message}!")


# 3. Coffee Orders

"""
get coffee
get size

if size == small
    price = 3
else if size == medium
    price = 4
else
    price = 5

if coffee != black
    price += 1
        
display price

"""

coffee = input("Coffee: ").lower()
size = input("Size: ").lower()

if size == "small":
    price = 3
elif size == "medium":
    price = 4
else:
    price = 5

if coffee != "black":
    price += 1


print("Cost: ", price)