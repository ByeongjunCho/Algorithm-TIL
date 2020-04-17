# 4837. [파이썬 S/W 문제해결 기본] 2일차 - 부분집합의 합


bits = [0] * 12
num = range(1,13)
result = [0]

# def subset(k, n, sub, K):
#     if k == n:
#         if sum(bits) == sub:
#             tmp = 0
#             for i in range(len(bits)):
#                 if bits[i]:
#                     tmp += num[i]
#             if tmp == K:
#                 result[0] += 1
#         return
#
#     bits[k] = 1; subset(k+1, n, sub, K)
#     bits[k] = 0; subset(k+1, n, sub, K)

def subset(k, n, cnt, cur_sum)  # cnt, cur_sum:원소들의 합
    global ans, N, K
    if cnt > N or cur_sum > K: return 0
    if k==n:
        if cnt == N and cur_sum == K:
            return 1
        else: return 0


    ret = 0
    ret += subset(k+1, n, cnt+1, cur_sum+k)
    ret += subset(k+1, n, cnt, cur_sum)

def subset(k, n, sub, K, cnt):
    if cnt > sub:
        return
    if k == n:
        if cnt == sub:
            tmp = 0
            for i in range(len(bits)):
                if bits[i]:
                    tmp += num[i]
            if tmp == K:
                result[0] += 1
        return

    bits[k] = 1; subset(k+1, n, sub, K, cnt+1)
    bits[k] = 0; subset(k+1, n, sub, K, cnt)

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    result[0] = 0
    subset(0,12, N, K, 0)
    print('#{} {}'.format(tc, result[0]))
