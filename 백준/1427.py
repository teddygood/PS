n = input()
number_list = []
for i in range(len(n)):
    number_list.append(n[i])

number_list.sort(reverse=True)

# print(*number_list)

for number in number_list:
    print(number, end='')