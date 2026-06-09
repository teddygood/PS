n = int(input())
milk_store = list(map(int, input().split()))

count = 0

for i in range(n):
    if milk_store[i] == count % 3:
        count += 1
print(count)
        