# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M or L: ")
# # Small Pizza (S): $15, Medium Pizza (M): $20,  Large Pizza (L): $25
# pepperoni = input("Do you want Pepperoni on your pizza? Y or N: ")
# # Pepperoni is a $ 3 add-on
# extra_cheese = input("Do you want extra cheese? Y or N: ")
# # Extra-Cheese is a $ 1 add-on
#
#
# # Determining Bill
# bill = 0
# # TODO 1: Work out how much they need to pay based on their size choice.
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else:
#     bill += 25
# # TODO 2: Work out how much to add to their bill based on their pepperoni choice.
# if pepperoni == "Y":
#     bill += 3
# # TODO 3: Work out their final amount based on whether if they extra cheese.
# if extra_cheese == "Y":
#     bill += 1
#
# print("Your bill is $" + str(bill))


def PizzaDeliveries():
    print("Welcome to Python Pizza Deliveries!")
    size = input("What size pizza do you want? S, M or L: ")
    pepperoni = input("Do you want Pepperoni on your pizza? Y or N: ")
    extra_cheese = input("Do you want extra cheese? Y or N: ")

    bill = 0
    if size == "S":
        bill += 15
    elif size == "M":
        bill += 20

    else:
        bill += 25

    if pepperoni == "Y":
        bill += 3

    if extra_cheese == "Y":
        bill += 1

    print("Your bill is $" + str(bill))

print(PizzaDeliveries())