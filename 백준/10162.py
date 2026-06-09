T = int(input())

time_list = [300, 60, 10]
count_list = [0, 0, 0]

if T % 10 != 0:
    print(-1)

else:
    for i in range(len(time_list)):
        count_list[i] += T // time_list[i]
        T %= time_list[i]

    for i in range(len(time_list)):
        print(count_list[i])