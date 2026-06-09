n = int(input())
x = map(int, input().split())
m = int(input())
array = map(int, input().split())

hashmap = {}

for i in x:
    if i in hashmap:
        hashmap[i] += 1
    else:
        hashmap[i] = 1

print(' '.join(str(hashmap[i]) if i in hashmap else '0' for i in array))