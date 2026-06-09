n = int(input())
s = []
result = []
temp = True
count = 1

for i in range(n):
    num = int(input())
    while count <= num:
        s.append(count)
        count += 1
        result.append('+')
    if s[-1] == num:
        s.pop()
        result.append('-')
    else:
        temp = False
if temp == False:
    print('NO')
else:
    for i in result:
        print(i)