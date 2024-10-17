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

BASE_SALARY = 5000

worker_level = int(input("Enter Worker Level: "))

while worker_level < 1 or worker_level > 10:
    print("Invalid Worker Level")
    worker_level = int(input("Enter Worker Level: "))

print("Worker Level: ", worker_level)
print(f"Salary: {BASE_SALARY * worker_level}" )

print(f"With work level {worker_level}, your salary is ${BASE_SALARY * worker_level:,.2f}")



# 2. Number Sequences

# a. odd number
"""
  for i from 1 To 100 with step 2 Do
    display i
"""

for i in range(1, 101, 2):
    print(i)

# b. Summer Olympic Years
"""
    repeat from 1896 To 2024 with step 4
        display i
"""
for i in range(1896, 2025, 4):
    print(i, end=" ")

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

num_terms = int(input("Enter number of terms: "))

first_term = 0
second_term = 1

for i in range(0,  num_terms):
    print(first_term, end=" ")
    first_term , second_term = second_term, first_term + second_term



# 3. Menus

"""
display menu (S)miley, (F)rowny, (Q)uit  

get choice

while choice != "q":
    if choice == "s":
        display :)
    elif choice == "f":
        display :(
    else:
        display Invalid choice
        display Menu: \n(S)miley \n(F)rowny \n(Q)uit)

    get choice

if choice == "q" :
    display Farewell
"""

print("Menu: \n(S)miley \n(F)rowny \n(Q)uit)")

choice = input("Enter your choice: ").lower()

while choice != "q":
    if choice == "s":
        print(":)")
    elif choice == "f":
        print(":(")
    else:
        print("Invalid choice")
        print("Menu: \n(S)miley \n(F)rowny \n(Q)uit)")

    choice = input("Enter your choice: ").lower()

if choice == "q" :
    print("Farewell")

# 4. Accumulation

# Average Age
"""
total_age = 0
iteration_counter = 0

get group_size

repeat group_size times
    get age
    if age < 1
        continue
          
    total_age += age
    iteration_counter += 1
    
display total_age
    
"""

total_age = 0
iteration_counter = 0

group_size = int(input("Enter group_size: "))

while iteration_counter < group_size:
    age = int(input("Enter age: "))
    if age < 1:
        continue
    total_age += age
    iteration_counter += 1

print(f"Average age {total_age/group_size:,.2f}")


#Smileys Count
"""
smileys_counter = 0
frownies_counter = 0

display menu (S)miley, (F)rowny, (Q)uit  

get choice

while choice != "q":
    if choice == "s":
        display :)
        smileys_counter = smileys_counter + 1
    elif choice == "f":
        display :(
        frownies_counter = frownies_counter + 1
    else:
        display Invalid choice
        display Menu: \n(S)miley \n(F)rowny \n(Q)uit

    get choice

if choice == "q" :
    display Farewell 
    display smileys_counter
    display frownies_counter
"""

smileys_counter = 0
frownies_counter = 0

print("Menu: \n(S)miley \n(F)rowny \n(Q)uit")
choice = input("Enter your choice: ").lower()

while choice != "q":
    if choice == "s":
        print(" :)")
        smileys_counter = smileys_counter + 1
    elif choice == "f":
        print(" :(")
        frownies_counter = frownies_counter + 1
    else:
        print("Invalid choice")
        print("Menu: \n(S)miley \n(F)rowny \n(Q)uit)")

    choice = input("Enter your choice: ").lower()

if choice == "q" :
    print(f"Farewell \nsmileys_counter: {smileys_counter} \nfrownies_counter: {frownies_counter}")


# Total Numbers
"""
sum = 0

get repetitions_number

repeat repetitions_number times
    get number
    sum = sum + number

display sum
"""

sum = 0

repetitions_number = int(input("How many numbers do you want to add up? "))

for i in range(repetitions_number):
    number = float(input(f"Enter number {i+1}: "))
    sum = sum + number

print(f"The total of those {repetitions_number} numbers is {sum:,.2f}")


# 5. Guessing Game

SECRET = 6
guess_counter = 0
guess = int(input("Guess a number: "))
while guess != SECRET:
    if guess < SECRET:
        print("Guess Higher")
    else:
        print ("Guess Lower")

    guess_counter += 1
    guess = int(input("Guess a number: "))

print(f"You got it in {guess_counter + 1} guesses!")


# 6. Nested Loops
"""
get rows
get columns

repeat rows times
    repeat columns times
        display columns iteration
"""

rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

for i in range(rows):
    for j in range(columns):
        print(j, end=" ")
    print(end="\n")