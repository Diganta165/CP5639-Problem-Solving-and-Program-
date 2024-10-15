# 1. Error Checking

"""
BASE_SALARY = 5000
get worker_level

while worker_level < 1 and worker_level > 100
    display "Invalid Worker Level"
    get worker_level

display worker_level
display salary BASE_SALARY* worker_level
"""

# BASE_SALARY = 5000
#
# worker_level = int(input("Enter Worker Level: "))
#
# while worker_level < 1 or worker_level > 10:
#     print("Invalid Worker Level")
#     worker_level = int(input("Enter Worker Level: "))
#
# print("Worker Level: ", worker_level)
# print(f"Salary: {BASE_SALARY * worker_level}" )
#
# print(f"With work level {worker_level}, your salary is ${BASE_SALARY * worker_level:,.2f}")



# 2. Number Sequences

# a. odd number
"""
  for i from 1 To 100 with step 2 Do
    display i
"""

# for i in range(1, 101, 2):
#     print(i)

# b. Summer Olympic Years
"""
    repeat from 1896 To 2024 with step 4
        display i
"""
# for i in range(1896, 2025, 4):
#     print(i, end=" ")

# c. Fibonacci Sequence
"""
    The fibonacci sequence represents a series where each number is the sum of previous two numbers.
    
    get num_terms
    
    first_term = 0
    second_term = 1
    
    repeat num_terms times
        display first_term
        first_term , second_term = second_term, first_term + second_term
"""

# num_terms = int(input("Enter number of terms: "))
#
# first_term = 0
# second_term = 1
#
# for i in range(0,  num_terms):
#     print(first_term, end=" ")
#     first_term , second_term = second_term, first_term + second_term



# 3. Menus

"""
display menu (S)miley, (F)rowny, (Q)uit  

get choice

while choice != "q" and choice != "s" and choice != "f":
        display "Invalid choice"
        display "Menu: \n(S)miley \n(F)rowny \n(Q)uit)"
        choice = input("Enter your choice: ")

if choice == "s":
    display ":)"
elif choice == "f":
    display ":("
else:
    display "Farewell"
"""

# print("Menu: \n(S)miley \n(F)rowny \n(Q)uit)")
#
# choice = input("Enter your choice: ").lower()
#
# while choice != "q" and choice != "s" and choice != "f":
#         print("Invalid choice")
#         print("Menu: \n(S)miley \n(F)rowny \n(Q)uit)")
#         choice = input("Enter your choice: ")
#
# if choice == "s":
#     print(":)")
# elif choice == "f":
#     print(":(")
# else:
#     print("Farewell")


# 4. Accumulation

# A. Sentinel
"""
SENTINEL = -1
total = 0
get value
while value != SENTINEL
    total = total + value
    get value
display total
"""

# SENTINEL = -1
# total = 0
#
# value = int(input("Enter value (to quit enter -1): "))
#
# while value != SENTINEL:
#     total += value
#     value = int(input("Enter value: "))
#
# print("The total is", total)



# B. Ask-the-user-to-quit
"""
total = 0
is_finished = False
while not is_finished
    get choice
    if choice is quit
         is_finished = True
    else
         get value
         total = total + value	
display total
"""
# total = 0
# is_finished = False
#
# while not is_finished:
#     choice = input("Enter your choice (enter 'quit' to finish or press enter to continue): ").lower()
#     if choice == "quit":
#         is_finished = True
#     else:
#         value = float(input("Enter your value: "))
#         total += value
#
# print(f"The total is {total:,.2f}")

# Average Age
"""

"""


