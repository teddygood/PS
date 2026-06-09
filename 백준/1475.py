num = input()

count = [0] * 10

for c in num:
    count[int(c)] += 1

count[6] = (count[6] + count[9] + 1) // 2
count[9] = 0   

print(max(count)) 
