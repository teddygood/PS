n = int(input())

for _ in range(n):
    a, b = input().split()
    if sorted(b) == sorted(a):
        print("Possible")
    else:
        print("Impossible")