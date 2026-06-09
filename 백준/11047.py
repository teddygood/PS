n, k = map(int, input().split())
a = []
count = 0

for i in range(n):
    a.append(int(input()))

for i in reversed(range(n)):
    count += k // a[i]
    k %= a[i]

print(count)