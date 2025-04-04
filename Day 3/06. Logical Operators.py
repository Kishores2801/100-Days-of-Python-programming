print("Welcome to the rollercoaster!")
height = int(input("What is your height in CM? "))

bill = 0

if height >= 120:
    print("You can ride the rollercoaster")

    # input age
    age = int(input("What is your age? "))

    if age < 12:
        bill = 5
        print("Child Tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth Tickets are $7")

    elif (age <= 45) and (age <= 55):
        bill=0
        print("Midlife crisis offer free tickets")

    else:
        bill = 12
        print("Adult tickets are $12")

    wants_photo = input("Do you want a photo taken? Y or N.")
    if wants_photo == "Y":
        bill += 3

    print(f"Your total bill is {bill}")


else:
    print("Sorry you are not eligible to ride the rollarcoaster")
