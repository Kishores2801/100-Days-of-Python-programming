height_input = int(input("Enter your height in cm: "))


bill = 0
if height_input >= 120:
    age = int(input("Enter your age: "))
    if age >= 18:
        bill += 12
        print("Adult tickets are $12")
    elif age >= 12:
        bill += 7
        print("Youth tickets are $7")
    else:
        bill += 5
        print("Child tickets are $5")
    need_photo = input("Do you need a photo? (y/n): ")
    if need_photo == "y":
        bill += 3
        print("Please pay $3 for picture")
    print("Your bill is:", bill)
else:
    print("You can't ride")



def rollercoaster_ride(height_input):
    bill = 0
    if height_input >= 120:
        age = int(input("Enter your age: "))
        if age >= 18:
            bill += 12
            print("Adult tickets are $12")
        elif age >= 12:
            bill += 7
            print("Youth tickets are $7")
        else:
            bill += 5
            print("Child tickets are $5")
        need_photo = input("Do you need a photo? (y/n): ")
        if need_photo == "y":
            bill += 3
            print("Please pay $3 for picture")
        print("Your bill is: $", bill)
    else:
        print("You can't ride")


rollercoaster_ride(height_input)