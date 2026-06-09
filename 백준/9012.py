# t = int(input())
#
# for _ in range(t):
#     parenthesis = list(input())
#     sum = 0
#
#     for i in parenthesis:
#         if i == "(":
#             sum += 1
#         elif i == ")":
#             sum -= 1
#         if sum < 0:
#             print("NO")
#             break
#
#     if sum > 0:
#         print("NO")
#     elif sum == 0:
#         print("YES")


t = int(input())

for _ in range(t):
    stack = []
    isVPS = True
    for ch in input():
        if ch == "(":
            stack.append(ch)
        else:
            if stack:
                stack.pop()
            else:
                isVPS = False
                break

    if stack:
        isVPS = False

    print("YES" if isVPS else "NO")