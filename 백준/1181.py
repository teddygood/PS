import sys

n = int(sys.stdin.readline())
str_list = []

for i in range(n):
    str_list.append(sys.stdin.readline().strip())

set_str_list = set(str_list)	# 중복값 제거
str_list = list(set_str_list)	

str_list.sort()
str_list.sort(key=len)	# 문자열 길이 순으로 정렬

for word in str_list:
    print(word)