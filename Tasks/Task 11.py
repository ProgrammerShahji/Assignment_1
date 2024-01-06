cost_per_unit = 100
discount_threshold = 1000
discount_percentage = 10

quantity = int(input("Enter the quantity: "))

total_cost = quantity * cost_per_unit

if total_cost > discount_threshold:
    discount = (discount_percentage / 100) * total_cost
    total_cost -= discount

print(f"The total cost is: Rs. {total_cost}")
