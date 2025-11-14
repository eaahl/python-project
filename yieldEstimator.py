bags = int(input("How many bags were harvested: "))
total = bags * 850
print("The bags cost a total of GHS", total)
if bags > 100:
    print("You also get a bonus of GHS 2000, therefore your new total is", total+2000)
