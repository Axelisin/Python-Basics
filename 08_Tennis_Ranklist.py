tournaments = int(input())
initial_points = int(input())

wins = 0
total_points = initial_points

for _ in range(tournaments):
    rounds = input()
    if rounds == "W":
        total_points += 2000
        wins += 1 
    elif rounds == "F":
        total_points += 1200
    elif rounds == "SF":
        total_points += 720

average_points = (total_points - initial_points) / tournaments
percent_wins = wins / tournaments * 100

print(f"Final points: {total_points}")
print(f"Average points: {int(average_points)}")
print(f"{percent_wins:.2f}%")
