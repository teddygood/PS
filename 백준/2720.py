t = int(input())
money_list = [25, 10, 5, 1]

answer = []

for _ in range(t):
    c = int(input())
    for n in money_list:
        answer.append(c//n)
        c %= n
print(*answer)