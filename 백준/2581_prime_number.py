# 소수 찾기
M = int(input())
N = int(input())

# M = 1
# N = 2
if M == 1:
    M = 2
prime_num = []
for i in range(M, N+1):
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            break
    else:
        prime_num.append(i)


if len(prime_num) == 0:
    print(-1)
else:
    print(sum(prime_num))
    print(prime_num[0])
