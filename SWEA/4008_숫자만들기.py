# 4008. [모의 SW 역량테스트] 숫자 만들기

# for tc in range(1, int(input()) + 1):
#     N = int(input())
#     calc = list(map(int, input().split()))
#     operator = []
#     # 계산자 만들기
#     operator += ['+'] * calc[0]
#     operator += ['-'] * calc[1]
#     operator += ['*'] * calc[2]
#     operator += ['/'] * calc[3]
#
#     numbers = list(map(int, input().split()))
#     def calculator(numbers, operators):
#         tmp = numbers[0]
#
#         for i in range(1, len(numbers)):
#             if operators[i-1] == '+':
#                 tmp += numbers[i]
#             elif operators[i-1] == '-':
#                 tmp -= numbers[i]
#             elif operators[i-1] == '*':
#                 tmp *= numbers[i]
#             elif operators[i-1] == '/':
#                 tmp = int(tmp / numbers[i])
#
#         return tmp
#
#
#     mymax = -10e10
#     mymin = 10e10
#
#     def perm(k):
#         if k == len(operator):
#             global mymax
#             global mymin
#             tmp = calculator(numbers, operator)
#             mymax = max(mymax, tmp)
#             mymin = min(mymin, tmp)
#             return
#         for i in range(k, len(operator)):
#             operator[k], operator[i] = operator[i], operator[k]
#             perm(k+1)
#             operator[k], operator[i] = operator[i], operator[k]
#
#     perm(0)
#     print('#{} {}'.format(tc, mymax - mymin))
def back(k, val):  # k: 반복횟수, 인덱스 val: 이전값
    global mymax
    global mymin
    if k == N:
        mymax = max(mymax, val)
        mymin = min(mymin, val)
        return

    # if not calc[1] and not calc[3] and val > mymin:
    #     return
    # if not calc[0] and not calc[2] and val < mymax:
    #     return

    for i in range(4):
        if calc[i] and i == 0:
            calc[i] -= 1
            back(k+1, val+nums[k])
            calc[i] += 1
        elif calc[i] and i == 1:
            calc[i] -= 1
            back(k + 1, val - nums[k])
            calc[i] += 1
        elif calc[i] and i == 2:
            calc[i] -= 1
            back(k+1, val * nums[k])
            calc[i] += 1
        elif calc[i] and i == 3:
            calc[i] -= 1
            back(k + 1, int(val/nums[k]))
            calc[i] += 1


for tc in range(1, int(input()) + 1):
    N = int(input())
    calc = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    mymax = -10e10
    mymin = 10e10
    back(1, nums[0])
    print('#{} {}'.format(tc, mymax - mymin))