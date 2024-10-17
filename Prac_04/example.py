MINIMUM_MONTH = 1
MAXIMUM_MONTH = 12

birth_month = int(input(f"Enter the month number ({MINIMUM_MONTH}-{MAXIMUM_MONTH}): "))
while birth_month < MINIMUM_MONTH or birth_month > MAXIMUM_MONTH:
    print("Invalid month")
    birth_month = int(input(f"Enter the month number ({MINIMUM_MONTH}-{MAXIMUM_MONTH}): "))

for count in range(1, birth_month + 1):
    print(count, end=" ")
print()