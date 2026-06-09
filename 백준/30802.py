import math

n = int(input())
size = list(map(int, input().split()))
t, p = map(int, input().split())
count = 0

for s in size:
    count += math.ceil(s / t)

print(count)
print(n // p, n % p)
