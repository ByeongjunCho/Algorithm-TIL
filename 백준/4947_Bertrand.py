# 베르트랑 공준

M = 46
N = 47


while True:
    M = int(input())
    if M == 0:
        break
    N = 2*M

    prime_num = []
    for i in range(M, N+1):
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                break
        else:
            prime_num.append(i)
    print(len(prime_num))