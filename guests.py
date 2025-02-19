guests = set()
user_guests = input("Enter a guest(q to quit): ")

while True:
    if user_guests.lower() == "q":
        print("You stopped adding guests, bye!")
        break
    else:
        guests.add(user_guests)
        print(guests)
    user_guests = input("Enter a guest(q to quit): ")
    