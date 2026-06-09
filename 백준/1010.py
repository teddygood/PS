import math

def combination(n, m):
    f = math.factorial
    return f(n) / (f(m) * f(n-m))


t = int(input())
results = []

for _ in range(t):
    n, m = list(map(int, input().split()))
    results.append(int(combination(m, n)))

for result in results:
    print(result)