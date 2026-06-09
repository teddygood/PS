n = int(input())
graph = []
num_list = []
count = 0
result = 0

for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x, y):
    # 범위 벗어나면 종료
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    # 현재 노드를 방문하지 않았다면
    if graph[x][y] == 1:
        global count
        count += 1
        # 현재 노드 방문 처리
        graph[x][y] = 0
        # 상하좌우 재귀적으로 호출
        # dfs(x-1, y)
        # dfs(x, y-1)
        # dfs(x+1, y)
        # dfs(x, y+1)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False

for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            num_list.append(count)
            result += 1
            count = 0

print(result)
num_list.sort()
print(*num_list)