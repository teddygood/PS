n, l = map(int, input().split())
point = list(map(int, input().split()))

point.sort()

start = point[0]
tape_count = 1

for loc in point[1:]:
    # 물이 새는 곳이 범위 내에 있다면
    if loc in range(start, start + l):
        continue
    else:
        start = loc # 없으면 그곳부터 다시 시작
        tape_count += 1 # 테이프 다시 붙이기

print(tape_count)