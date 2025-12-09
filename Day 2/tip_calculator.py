print("Welcome to the tip calculator!")
bill = input("What was the total bill? ")
tip = input("How much tip would you like to give? 0, 5, 10, 12 or 15 %? ")
people = input("How many people split the bill? ")

tip_decimal = int(tip) / 100

bill_split = round((float(bill)*tip_decimal + float(bill))/ int(people),2)

print(f"Each person should pay:${bill_split}")