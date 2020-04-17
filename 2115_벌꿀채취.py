# SWEA 2115. [모의 SW 역량테스트] 벌꿀채취

def makemaxmap():
    for i in range(N):
        for j in range(N-M+1):
            makeMaxSubset(i, j, 0, 0, 0)

# i: 행, j: 열, cnt: 고려한원소수
# sum: 부분집합에 속한 원소의 합
# powSum: 부분집합에 속한 원소의 이익
def makeMaxSubset(i, j, cnt, sum, powSum):
    if sum > C: # 부분집합의 합은 목표량C를 초과하면 리턴
        return
    if cnt == M:
        if maxMap[i][j-M] < powSum:
            maxMap[i][j - M] = powSum
        return


    # 선택
    makeMaxSubset(i, j+1, cnt+1, sum+arr[i][j], powSum+(arr[i][j]**2))
    # 비선택
    makeMaxSubset(i, j + 1, cnt + 1, sum, powSum)

def getMaxBenefit():
    max = 0  # 조합적 선택후 최대이익값
    temp = 0

    # 1. 일꾼 A를 기준으로 선택
    for i in range(N):
        for j in range(N-M+1):
            # 2. 일꾼 B 선택
            # 2.1 같은행 기준
            for j2 in range(j+M, N-M+1):
                temp = maxMap[i][j] + maxMap[i][j2]
                if max < temp:
                    max = temp

            # 다음행부터 마지막까지 선택
            for i2 in range(i+1, N):
                for j2 in range(N-M+1):
                    temp = maxMap[i][j] + maxMap[i2][j2]
                    if max < temp:
                        max = temp
    return max
T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxMap = [[0 for _ in range(N)] for _ in range(N)]

    # 1. 각 위치에서 연속된 M개를 고려해 취할 수 있는 부분집합의 최대값 선택
    makemaxmap()
    # 2. 최대값 출력
    print("#{} {}".format(tc, getMaxBenefit()))