n = int(input())
num = []

for _ in range(n):
    x = int(input())
    num.append(x)

for i in sorted(num):
    print(i)

# import sys

# input()
# arr = sorted(map(int, sys.stdin.read().split()))
# sys.stdout.write('\n'.join(map(str,arr)))