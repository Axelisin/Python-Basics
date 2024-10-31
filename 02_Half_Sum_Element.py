import sys

n = int(input())
max_num = -sys.maxsize
summ_num = 0

for _ in range(n):
    new_num = int(input())
    summ_num += new_num
    if new_num > max_num:
        max_num = new_num

if max_num == summ_num - max_num:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    print("No")
    print(f"Diff = {abs(max_num - (summ_num - max_num))}")
