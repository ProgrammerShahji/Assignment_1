units = int(input("Enter the number of units consumed: "))

if units <= 100:
    bill_amount = 0

elif units <= 300:
    bill_amount = (units - 100) * 5

else:
    bill_amount = (200 * 5) + (units - 300) * 10

print(f"The total electricity bill amount is Rs.{bill_amount}")
