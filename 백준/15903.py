n, m = map(int, input().split())
card = list(map(int, input().split()))
s = 0

for _ in range(m):
    card.sort()
    
    s = card[0] + card[1]
    card[0] = s
    card[1] = s

print(sum(card))