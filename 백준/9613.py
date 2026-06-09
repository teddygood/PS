from itertools import combinations

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

t = int(input())
lists = []

for _ in range(t):
    lists = list(map(int, input().split()))
    lists = lists[::-1]
    del lists[len(lists) - 1]
    comb = combinations(lists, 2)

    result = 0
    for comb_list in comb:
        result += gcd(comb_list[0], comb_list[1])
    print(result)