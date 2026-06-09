word = input().strip()

count = [0] * 26

for c in word:
    count[ord(c) - ord('a')] += 1

print(' '.join(map(str, count)))