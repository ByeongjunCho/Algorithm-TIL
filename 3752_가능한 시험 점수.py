# 3752. 가능한 시험 점수

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     vals = list(map(int, input().split()))
#     result = {0}
#
#     for i in range(N):
#         tempSet = result.copy()
#         for val in tempSet:
#             result.add(val+vals[i])
#     print("#{} {}".format(tc, len(result)))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    vals = list(map(int, input().split()))
    mymax = 0  # 현재까지의 최대점수
    score = [0] * (sum(vals) + 1)
    score[0] = 1
    for val in vals:
        for i in range(mymax, -1, -1):
            if score[i]:
                score[i+val] = 1
        mymax += val
    print("#{} {}".format(tc, sum(score)))

"""인덱스에 마이너스를 하는 방식"""
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    vals = list(map(int, input().split()))
    mymax = 0  # 현재까지의 최대점수
    score = [0] * (sum(vals) + 1)
    score[0] = 1
    for val in vals:
        for i in range(mymax+val, mymax, -1):
            if i - val < 0: break
            if score[i-val]:
                score[i] = 1
        mymax += val
    print("#{} {}".format(tc, sum(score)))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    vals = map(int, input().split())
    a = 1
    for val in vals:
         a |= a << val

    print("#{} {}".format(tc, bin(a).count('1')))
