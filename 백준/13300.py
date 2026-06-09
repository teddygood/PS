n, k = map(int, input().split())

room = [[0] * 7 for _ in range(2)]

for _ in range(n):
    s, y = map(int, input().split())
    room[s][y] += 1

count = 0
for s in range(2):
    for y in range(1, 7):
        if room[s][y] > 0:
            count += (room[s][y] - 1) // k + 1 # math.ceil(n / k)

print(count)

