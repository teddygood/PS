# 처음 생각한 풀이
# n = int(input())

# array = []
# result = 0

# for i in range(n):
#     array.append(int(input()))

# while len(array) != 1:
#     array.sort()
#     result = array[0] + array[1]
#     array.remove(array[0], array[1])
#     array.append(result)

# print(result)

import heapq

n = int(input())

heap = []
result = 0
sum_value = 0

for i in range(n):
    heapq.heappush(heap, int(input()))

while len(heap) != 1:
    sum_value = heapq.heappop(heap) + heapq.heappop(heap)
    result += sum_value
    heapq.heappush(heap, sum_value)
    
print(result)