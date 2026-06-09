first = int(input())
second = input()
second_list = list(map(int, second))

second_reverse = second_list[::-1]
result = 0

for i in range(len(second)):
    print(first*second_reverse[i])

print(first * int(second))