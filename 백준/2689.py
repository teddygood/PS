import math

a, b, v = map(int, input().split())

# (a-b)n - b = v
# 정상에 올라간 후에는 미끄러지지 않는다. -> -b

day = (v - b) / (a - b) 

print(math.ceil(day))