n = int(input())
test_num = list(map(int, input().split()))
m = max(test_num)

for i in range(n):
    test_num[i] = test_num[i] / m * 100
avg = sum(test_num) / n
print(avg)