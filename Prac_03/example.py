# Testing

"""
get choice
if choice == "rare"
    display "2 minutes"
else if choice == "medium"
    display "4 minutes"
else if choice == "well-done"
    display "6 minutes"
else if choice == "burnt"
    display "8 minutes"
else
   display error message
"""

choice = input("Steak choice (rare, medium, well-done or burnt):)").lower()

if choice == "rare":
    print("2 minutes")
elif choice == "medium":
    print("4 minutes")
elif choice == "well-done":
    print("6 minutes")
elif choice == "burnt":
    print("8 minutes")
else:
    print("Ain't no steak like that here")