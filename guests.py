guests = set()
user_guests = input("Enter a guest(q to quit): ")

while True:
    #stops the program when the user enters q
    if user_guests.lower() == "q":
        print("You stopped adding guests, bye!")
        break
    else:
        if user_guests == "":
            print("Guest name can't be empty")
        else:
        # Allows users to add guests to the list
            guests.add(user_guests.capitalize())
            print(guests)
    user_guests = input("Enter a guest(q to quit): ")

    if user_guests in guests:
        print(f"{user_guests} already exists")
print() 

print("Your guests")
for guest in guests:
    print(f"* {guest}")


