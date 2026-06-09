n = int(input())
a = list(map(int, input().split()))
x = int(input())

exist = [0] * 2000001
count = 0

for num in a:
    exist[num] = 1

for num in a:
    target = x - num
    if 0 < target <= 1000000 and exist[target]:
        count += 1

print(count // 2)  # 쌍이 중복으로 세어지므로 나누기 2를 해야 한다. e.g., (1,12), (12,1)
