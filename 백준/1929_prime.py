# 소수 구하기

M, N = list(map(int, input().split()))

for i in range(M, N+1):
    # 소수 판별기
    if i == 1:
        continue
    for k in range(2, i//2 + 1):
        if i % k == 0:
            break
    else:
        print(i)

