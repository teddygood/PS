n = int(input())

cups = [1, 2, 3]

for _ in range(n):
    x, y = map(int, input().split())

    x = cups.index(x)
    y = cups.index(y)
    cups[x], cups[y] = cups[y], cups[x]

print(cups[0])
