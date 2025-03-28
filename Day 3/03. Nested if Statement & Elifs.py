print("Welcome to the the roller coaster!")
height = int(input("What is your height in cm? "))



# if height >= 120:
#     age = int(input("What is your age in years? "))
#     if age <= 18:
#         print("You can ride the rollercoaster, Your ticket price is $7")
#     else:
#         print("You can ride the rollercoaster, Your ticket price is $12")
# else:
#     print("Sorry You can't ride the rollercoaster")



if height >= 120:
    age = int(input("What is your age in years? "))
    if age <= 12:
        print("You can ride the rollercoaster, Your ticket price is $5")
    elif age <= 18:
        print("You can ride the rollercoaster, Your ticket price is $7")
    else:
        print("You can ride the rollercoaster, Your ticket price is $12")
else:
    print("Sorry You can't ride the rollercoaster")