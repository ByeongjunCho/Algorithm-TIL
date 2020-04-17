# 4837. [파이썬 S/W 문제해결 기본] 2일차 - 부분집합의 합

def subsetSum(N, K):  # N=원소의 개수, K=부분집합의 합
    count_K = 0
    for i in range(2**12):
        count = 0
        subsum = 0
        for j in range(12):
            if count > N: break
            if i&1<<j:
                count += 1
                subsum += 12-j
        if count != N:
            continue
        elif subsum == K:
            count_K+=1
    return count_K

test_case = int(input())
for T in range(1, test_case+1):
    N, K = map(int, input().split())
    print('#{} {}'.format(T, subsetSum(N,K)))