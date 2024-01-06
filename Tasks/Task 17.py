age = int(input("Enter age: "))
gender = input("Enter gender (M or F): ").upper()
marital_status = input("Enter marital status (Y or N): ").upper()

if gender == 'F':
    print("She will work only in urban areas.")
elif gender == 'M' and 20 <= age <= 40:
    print("He may work anywhere.")
elif gender == 'M' and 40 <= age <= 60:
    print("He will work in urban areas only.")
else:
    print("ERROR")
