n = int(input())
n_list = list(map(int, input().split()))
count = 0

sieve = [True] * 1001
sieve[0], sieve[1] = [False] * 2
for i in range(2, int(1001 ** 0.5) + 1):
    if sieve[i] == True:
        for j in range(i+i, 1001, i):
            sieve[j] = False

for num in n_list:
    if sieve[num]:
        count += 1

print(count)