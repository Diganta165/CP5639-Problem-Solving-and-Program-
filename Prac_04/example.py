MINIMUM_MONTH = 1
MAXIMUM_MONTH = 12

birth_month = int(input("Enter the month number (1-12): "))
while birth_month < 1 or birth_month > 12:
    print("Invalid month")
    birth_month = int(input("Enter the month number (1-12): "))

for count in range(1, birth_month + 1):
    print(count, end=" ")
print()

# Using the format method:
month = int(input("Enter the month number ({}-{}): ".format(MINIMUM_MONTH, MAXIMUM_MONTH)))

# Using string concatenation and explicit type conversion
month = int(input("Enter the month number (" + str(MINIMUM_MONTH) + "-" + str(MAXIMUM_MONTH) + "): "))

# Using f-strings
month = int(input(f"Enter the month number ({MINIMUM_MONTH}-{MAXIMUM_MONTH}): "))