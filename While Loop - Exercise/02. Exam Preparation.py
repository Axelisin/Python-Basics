number_of__bad_scores = int(input())

count_bad_scores = 0
last_problem = ""
total_score = 0
score_count = 0
is_enough = False

quiz_name = input()

while quiz_name != "Enough":
    score = int(input())
    total_score += score
    score_count += 1
    last_problem = quiz_name

    if score <= 4:
        count_bad_scores +=1
        if count_bad_scores == number_of__bad_scores:
            is_enough = True
            break
    
    quiz_name = input()


if is_enough:
    print(f"You need a break, {number_of__bad_scores} poor grades.")
else:
    print(f"Average score: {(total_score / score_count):.2f}")
    print(f"Number of problems: {score_count}")
    print(f"Last problem: {last_problem}")
