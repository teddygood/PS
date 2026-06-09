# def fib(n):
#     if n <= 1:
#         return n

#     return fib(n-1) + fib(n-2)

import sys

input = sys.stdin.readline
# T = int(sys.stdin.readline().rstrip())
T = int(input())

fib = [0, 1] # f0, f1
for i in range(2,46): # ƒ46의 값 1,134,903,170까지 계산
    fib.append(fib[i-1] + fib[i-2])

for _ in range(T):
    n = int(input())
    t_list = []

    # 문제에서 n의 최대 값은 1,000,000,000이고 ƒ46의 값이 1,134,903,170
    for i in range(45, 0, -1):
        if fib[i] <= n:
            t_list.append(fib[i])
            n -= fib[i]
        if n == 0:
            t_list.sort()
    print(*t_list)

# for _ in range(t_num):
#     t = int(input())

#     for i in range(t):
#         if fib(i) > t:
#             t -= fib(i-1)
#             t_list.append(fib(i-1))
#             break
#         i += 1
