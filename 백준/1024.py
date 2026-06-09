n, l = map(int, input().split())

for i in range(l, 101):
    x = n - (i * (i - 1) / 2)

    if x % i == 0 and x // i >= 0:
        x = int(x / i)
        
        for j in range(i):
            print(x+j, end=' ')
        break
else:
    print(-1)
