change = 1000 - int(input())
money_list = [500, 100, 50, 10, 5, 1]
count = 0
for money in money_list:
    count += change // money
    change %= money
print(count)