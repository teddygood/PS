text = input().lower()
text_list = list(set(text))
count_list = []


for i in text_list:
    count = text.count(i)
    count_list.append(count)

if count_list.count(max(count_list)) > 1:
    print('?')
else:
    print(text_list[count_list.index(max(count_list))].upper())