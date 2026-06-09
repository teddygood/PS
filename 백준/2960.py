n, k = map(int, input().split())

sieve = [False for _ in range(n+2)]
cnt = 0

for i in range(2, n+1):
    if sieve[i] == False:
        for j in range(i, n+1, i):
            if sieve[j] == False:
                sieve[j] = True
                cnt += 1

                if cnt == k:
                    print(j)
                    break