import sys

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

start = 0
end = max(array)

while start <= end:
    mid = (start + end) // 2
    num = 0

    for value in array:
        if value >= mid:
            num += mid
        else:
            num += value
    if num > m:
        end = mid - 1
    else:
        start = mid + 1

print(end)