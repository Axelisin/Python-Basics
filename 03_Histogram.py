n = int(input())

p1 = p2 = p3 = p4 = p5 = 0

for _ in range(n):
    new_num = int(input())
    if new_num < 200:
        p1 += 1
    elif new_num <= 399:
        p2 += 1
    elif new_num <= 599:
        p3 += 1
    elif new_num <= 799:
        p4 += 1
    elif new_num >= 800:
        p5 += 1

percent_p1 = p1 / n * 100
percent_p2 = p2 / n * 100
percent_p3 = p3 / n * 100
percent_p4 = p4 / n * 100
percent_p5 = p5 / n * 100

print(f"{percent_p1:.2f}%")
print(f"{percent_p2:.2f}%")
print(f"{percent_p3:.2f}%")
print(f"{percent_p4:.2f}%")
print(f"{percent_p5:.2f}%")
