n, m = map(int, input().split())
og = []
result = []

for _ in range(n):
    og.append(input())

# 행열에서 8x8로 자르기 위한 시작점 경우의 수
for i in range(n-7):
    for j in range(m-7):
        w_start = 0
        b_start = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                # 8x8에서 행렬의 인덱스 합이 짝수이면 시작점과 색이 같다.
                if (k+l) % 2 == 0:
                    if og[k][l] != 'B':
                        w_start += 1
                    if og[k][l] != 'W':
                        b_start += 1
                else:
                    if og[k][l] != 'W':
                        w_start += 1
                    if og[k][l] != 'B':
                        b_start += 1
        result.append(w_start)
        result.append(b_start)

print(min(result))
