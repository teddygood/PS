while True:
    a = list(map(int, input().split()))
    h = max(a)
    a.remove(h)

    if sum(a) == 0:
        break
    if a[0] ** 2 + a[1] ** 2 == h ** 2:
        print('right')
    else:
        print('wrong')