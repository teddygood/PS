n = int(input())
num_list = list(map(int, input().split()))
v = int(input())

# print(num_list.count(v)) 이렇게 해도 풀린다.

count = 0
for num in num_list:
    if num == v:
        count += 1

print(count)