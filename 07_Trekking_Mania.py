num_groups = int(input())

p1 = p2 = p3 = p4 = p5 = 0

for _ in range(num_groups):
    people = int(input())
    if people < 6:
        p1 += people
    elif people <= 12:
        p2 += people
    elif people <= 25:
        p3 += people
    elif people <= 40:
        p4 += people
    elif people > 40:
        p5 += people
  
total_pp = p1 + p2 + p3 + p4 + p5

print(f"{p1 / total_pp * 100:.2f}%")
print(f"{p2 / total_pp * 100:.2f}%")
print(f"{p3 / total_pp * 100:.2f}%")
print(f"{p4 / total_pp * 100:.2f}%")
print(f"{p5 / total_pp * 100:.2f}%")
