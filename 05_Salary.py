n = int(input())
salary = int(input())

for _ in range(n):
    website = input()
    if website == "Facebook":
        salary -= 150
    elif website == "Instagram":
        salary -= 100
    elif website == "Reddit":
        salary -= 50

    if salary <= 0:
        break

if salary <= 0:
    print(f"You have lost your salary.")
else:
  print(int(salary))
