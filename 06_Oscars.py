actor_name = input()
starting_points = float(input())
judges = int(input())
NOMINEE = 1250.5

total_points = starting_points

for _ in range(judges):
    judge_name = input()
    judge_points = float(input())
    points_recieved = (len(judge_name) * judge_points) / 2
    total_points += points_recieved
    if total_points > NOMINEE:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.2f}!")
        break

# if total_points > NOMINEE:
#     print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.2f}!")

# this is for..else structure here, else used if no BREAK occured
else:
    points_needed = NOMINEE - total_points
    print(f"Sorry, {actor_name} you need {points_needed:.2f} more!")
