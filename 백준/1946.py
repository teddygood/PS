import sys

t = int(input())

for i in range(t):
    
    people = []
    count = 1

    n = int(input())

    for i in range(n):
        doc, interview = map(int, sys.stdin.readline().split())
        people.append([doc, interview])

    people.sort()
    min_rank = people[0][1]

    for i in range(1, n):
        if people[i][1] < min_rank:
            min_rank = people[i][1]
            count += 1

    print(count)