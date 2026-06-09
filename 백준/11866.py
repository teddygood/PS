# import sys
# from collections import deque

# input = sys.stdin.readline

# n, k = map(int, input().split())
# queue = deque([x for x in range(1, n+1)])
# removed = []

# while queue:
#     queue.rotate(1-k)
#     removed.append(queue.popleft())

# print(f'<{", ".join(map(str, removed))}>')

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
queue = [x for x in range(1, n+1)]
removed = []
now = k-1

while queue:
    removed.append(queue.pop(now))
    # k번째 숫자를 제거하면 숫자들의 인덱스가 바뀌므로 now를 조정해줘야함
    if queue:
        now = (now+k-1) % len(queue)

print(f'<{", ".join(map(str,removed))}>')