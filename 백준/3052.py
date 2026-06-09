r_list = []

for _ in range(10):
    n = int(input())
    r_list.append(n % 42)

print(len(set(r_list)))