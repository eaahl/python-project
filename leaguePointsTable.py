teams = [
    {"name":"Kotoko", "points":25},
    {"name":"Hearts", "points":23},
    {"name":"Aduana Stars", "points":18}
]

print("The teams in the league are as follows")
for team in teams:
    print(team)

update = input("\nWhich team's points do you want to update: ").lower()
newpoints = int(input("What is the new points for the team: "))
if update == 'kotoko':
    teams[0]['points']= newpoints
elif update == 'hearts':
    teams[1]['points']= newpoints
elif update == 'aduana stars':
    teams[2]['points']= newpoints
else:
    print("This team is not in the league")

print("\n The updated league table is as follows")
for team in teams:
    print(team)
