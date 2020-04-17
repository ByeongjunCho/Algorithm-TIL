# {A, B, C} => 3! = 6
# 순열: 첫번째 위치에 올 것을 선택
#       두번째 위치 ........
#         A                B               C
#     B      C        A         C            ....
# C             B
# 실제로는 인덱스 기록

arr = 'ABC'; N = len(arr)
order = [0] * N # 실제 요소들의 순서(index를 기록)

# 중복순열
# for i in range(N):
#     for j in range(N):
#         for k in range(N):
#             print(arr[i], arr[j], arr[k])

for i in range(N):
    for j in range(N):
        if i == j: continue
        for k in range(N):
            if i == k or j==k: continue
            print(arr[i], arr[j], arr[k])

# 재귀 순열
def perm(k, n):
    if k == n:
        for i in range(N):
            print(arr[order[i]], end=' ')
        print()
        return
    used = [False] * N  # 지금까지 선택한 원소들의 집합
    for i in range(k):  # 지금까지 선택한 k개의 원소를 확인
        used[order[i]] = True
    for i in range(N):    # 선택하지 않은 요소들에 대해
        if used[i]:continue
        order[k] = i
        perm(k+1, n)

used = [0] * N  # 지금까지 선택한 원소들의 집합
def perm(k, n):
    if k == n:
        for i in range(N):
            print(arr[order[i]], end=' ')
        print()
        return

    for i in range(N):    # 선택하지 않은 요소들에 대해
        if used[i]:continue
        used[i] = 1
        order[k] = i
        perm(k+1, n)
        used[i] = 0
perm(0, N)


def perm(k, n, used):
    if k == n:
        for i in range(N):
            print(arr[order[i]], end=' ')
        print()
        return

    for i in range(N):  # 선택하지 않은 요소들에 대해
        if used & (1 << i): continue
        order[k] = i
        perm(k+1, n, used | (1 << i))

perm(0, N, 0)