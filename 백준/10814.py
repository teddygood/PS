n = int(input())
p_list = []

for i in range(n):
    age, name = map(str, input().split())
    age = int(age)
    p_list.append((age, name))

p_list.sort(key=lambda x: x[0])

for i in p_list:
    print(i[0], i[1])