# cricket_tournament.py

team = input("Enter team name: ")

matches = int(input("Enter matches played: "))

wins = int(input("Enter matches won: "))

losses = matches - wins

points = wins * 2

print("Team Name:", team)
print("Matches Played:", matches)

print("Matches Won:", wins)
print("Matches Lost:", losses)

print("Total Points:", points)

if points >= 10:
    print("Qualified for Semi Finals")
else:
    print("Not Qualified")

captain = input("Enter captain name: ")

print("Captain Name:", captain)

for i in range(3):
    print("Tournament Record Updated")

print("Cricket Tournament Management System")
print("Thank You")