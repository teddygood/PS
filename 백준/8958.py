t_num = int(input())

for i in range(t_num):
    t = list(input())
    sum = 0
    c = 1
    for i in t:
        if i == 'O':
            sum += c
            c += 1
        else:
            c = 1
    print(sum)