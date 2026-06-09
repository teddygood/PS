import heapq
import sys

n = int(input())
heap = []

for _ in range(n):
    x = int(sys.stdin.readline())

    if x != 0:
        heapq.heappush(heap, (abs(x), x))
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)
        # print(hq.heappop(heap)[1] if heap else 0)