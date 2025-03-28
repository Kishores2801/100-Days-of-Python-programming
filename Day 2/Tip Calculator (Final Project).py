print("Welcome to the Tip Calculator!")
bill_charged = float(input("What was the total bill? $"))
tip_percent = int(input("How much tip would you like to give? 10, 12, or 15? "))
people_split = int(input("How many people to split the bill? "))

# Calculating a total bill values
total_bill = (bill_charged * (tip_percent)/100) + bill_charged

# Calculating Bill share
bill_share = round(total_bill / people_split,2)


# Final output
print(f"Each person should pay: ${bill_share}")
