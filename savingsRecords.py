ladies = {'Akosua':200, 'Ama':150, 'Adwoa':300}
print("\nSaving progress of the following ladies")
for name,amount in ladies.items():

    print(name, "||", amount)

update = input("\nWho's savings do you want to update: ").title()
newAmount = int(input("What is the new savings amount: "))
if update == 'Akosua':
    ladies['Akosua']= newAmount
elif update == 'Ama':
    ladies['Ama']= newAmount
elif update == 'Adwoa':
    ladies['Adwoa']= newAmount
else:
    print("This lady does not exist in our records")

print("\n The updated savings list is as follows")
for name,amount in ladies.items():

    print(name, "||", amount)
