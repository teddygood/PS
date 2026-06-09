import sys

n = int(sys.stdin.readline())
s = []
for i in range(n):
    s.append(list(map(int, sys.stdin.readline().split())))
s.sort(key=lambda x: (x[1], x[0]))
for i in s:
    print(i[0], i[1])