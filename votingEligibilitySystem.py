#taking inputs
name = input("Please enter your full name: ")
age = int(input("Please enter your age: "))
nationality = input("What is your nationality: ").lower()

#validations
if age >= 18 and nationality == 'ghanaian':
    print(f"{name}, you are eligible to vote!")
else:
    print(f"{name}, you are not eligible to vote.")
