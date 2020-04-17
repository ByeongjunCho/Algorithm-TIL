N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 콤비네이션 경우의 수를 구한다
v1 = 1
for i in range(N, (N>>1), -1):
    v1 *= i
v2 = 1
for j in range(1, (N>>1) + 1):
    v2 *= j

cn = v1 // v2   # 콤비네이션 출력개수

case = set(range(N))
order = [0] * N
memo = []
def combi(k, start):
    if len(memo) == cn >> 1:   # 경우의 수보다 반 작게 사용 가능
        return
    if k == (N>>1):
        s_idx = order[:(N>>1)]  # start팀 번호
        l_idx = case - set(s_idx) # link팀 번호

        s_val = 0
        for i in s_idx:
            for j in s_idx:
                s_val += arr[i][j]
        l_val = 0
        for i in l_idx:
            for j in l_idx:
                l_val += arr[i][j]
        memo.append(abs(s_val - l_val))

    for i in range(start, N):
        order[k] = i
        combi(k+1, i+1)

combi(0, 0)
print(min(memo))
