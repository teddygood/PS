def Eratos(n):
    if n == 1:
        return False

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

t = int(input())

for _ in range(t):
    n = int(input())
    a = n // 2
    b = n // 2

    while a > 0:
        if Eratos(a) and Eratos(b):
            print(a, b)
            break
        # n을 반으로 나눈 후 a, b를 각각 -1, 1씩 증가시키면서 모두 소수인지 확인 
        else:
            a -= 1
            b += 1