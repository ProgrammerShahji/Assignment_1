number = int(input("Enter a number: "))

last_digit = number % 10

if last_digit % 3 == 0:
    print(f"The last digit ({last_digit}) is divisible by 3.")
else:
    print(f"The last digit ({last_digit}) is not divisible by 3.")
