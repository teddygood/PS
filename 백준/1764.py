import sys

n, m = map(int, sys.stdin.readline().split())

n_list = [sys.stdin.readline().strip() for _ in range(n)]
m_list = [sys.stdin.readline().strip() for _ in range(m)]

result = list(set(n_list) & set(m_list))

print(len(result))

for i in sorted(result):
    print(i)