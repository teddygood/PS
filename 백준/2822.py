score = []
result = []
score_sum = 0

# score = [int(input()) for i in range(8)]

for _ in range(8):
    score.append(int(input()))

for i in sorted(score, reverse=True)[:5]:
    result.append(score.index(i))
    score_sum += i

print(score_sum)

for i in sorted(result):
    print(i+1, end=' ')