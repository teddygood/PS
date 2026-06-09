T = int(input())

for _ in range(T):
    n = int(input())

    d = [0] * n

    for i in range(2, n+1):
        for j in range(2, n+1):
            if j % i == 0 and d[j-1] == 0:
                d[j-1] = 1
            elif j % i == 0 and d[j-1] == 1:
                d[j-1] = 0
    result = d.count(0)
    print(result)