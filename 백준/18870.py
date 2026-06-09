n = int(input())

x_list = list(map(int, input().split()))

sort_list = sorted(set(x_list))
index_dict = {sort_list[i]:i for i in range(len(sort_list))}

print(*[index_dict[i] for i in x_list])
