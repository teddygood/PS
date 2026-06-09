n, m = map(int, input().split())

space = [[0] * m for _ in range(n)]

x, y, d = map(int, input().split())

# 현재 방문 처리 
space[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽 회전 함수
def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

count = 1
turn_time = 0

while True:
    turn_left()
    nx = x + dx[d]
    ny = y + dy[d]
    
    # 회전 이후 정면에 가보지 않은 칸이 존재하는 경우
    if space[nx][ny] == 0 and array[nx][ny] == 0:
        space[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    
    # 회전 이후 정면에 가보지 않은 칸이 없거나 벽인 경우
    else:
        turn_time += 1
    
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        # 뒤로 갈 수 있다면 이동
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 벽인 경우
        else:
            break
        turn_time = 0

print(count)    