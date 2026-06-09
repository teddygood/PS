n, x = map(int, input().split())

integer = list(map(int, input().split()))

for i in range(len(integer)):
    if integer[i] < x:
        print(integer[i], end=" ")