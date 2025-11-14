passenger_route= input("Enter the passenger route: ")
passengers= int(input("Enter the total number of passengers boarding the trotro: "))
fare = 0
if passenger_route =="madina":
    fare = 5
elif passenger_route =="kasoa":
    fare = 10
elif passenger_route =="Tema":
    fare = 8
print(f"Route: {passenger_route} \nFare: GHS {fare} \nPassengers: {passengers}")
totalFare = passengers * fare
print("The total fare for the trip is GHS",totalFare)
