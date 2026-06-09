def Eratos(m, n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 지정
    n += 1
    sieve = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(2 * i, n, i):  # i 이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 출력
    for i in range(m, n):
        if i > 1 and sieve[i] == True:
            print(i)

m, n = map(int, input().split())
Eratos(m, n)
