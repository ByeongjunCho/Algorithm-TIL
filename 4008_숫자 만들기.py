# 4008. [모의 SW 역량테스트] 숫자 만들기

# def back(k, val):  # k: 반복횟수, 인덱스 val: 이전값
#     global mymax
#     global mymin
#     if k == N:
#         mymax = max(mymax, val)
#         mymin = min(mymin, val)
#         return
#
#     for i in range(4):
#         if operators[i] and i == 0:
#             operators[i] -= 1
#             back(k+1, val+nums[k])
#             operators[i] += 1
#         elif operators[i] and i == 1:
#             operators[i] -= 1
#             back(k + 1, val - nums[k])
#             operators[i] += 1
#         elif operators[i] and i == 2:
#             operators[i] -= 1
#             back(k+1, val * nums[k])
#             operators[i] += 1
#         elif operators[i] and i == 3:
#             operators[i] -= 1
#             back(k + 1, int(val/nums[k]))
#             operators[i] += 1
#
# for tc in range(1, int(input()) + 1):
#     N = int(input())
#     operators = list(map(int, input().split()))
#     nums = list(map(int, input().split()))
#
#     mymax = -10e10
#     mymin = 10e10
#     back(1, nums[0])
#     print('#{} {}'.format(tc, mymax - mymin))



def func(n, k, r, op1, op2, op3, op4):
    global maxVal, minVal
    if n == k:
        maxVal = max(maxVal, r)
        minVal = min(minVal, r)
        return

    if op1:
        func(n + 1, k, r + nums[n], op1-1, op2, op3, op4)
    if op2:
        func(n + 1, k, r - nums[n], op1, op2-1, op3, op4)
    if op3:
        func(n + 1, k, r * nums[n], op1, op2, op3-1, op4)
    if op4:
        func(n + 1, k, int(r/nums[n]), op1, op2, op3, op4-1)

for tc in range(1, int(input()) + 1):
    N = int(input())
    op1, op2, op3, op4 = map(int, input().split())
    nums = list(map(int, input().split()))
    maxVal = -10e10
    minVal = 10e10
    func(1, N, nums[0], op1, op2, op3, op4)
    print("#{} {}".format(tc, maxVal - minVal))