n = int(input())

c_result = 100
s_result = 100

for _ in range(n):
    c, s = map(int, input().split())

    if c > s:
        s_result -= c
    elif c < s:
        c_result -= s
    else:
        pass

print(c_result, s_result)
