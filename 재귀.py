# 재귀를 이용한 부분집합

A = [1,2,3]
b = [0, 0, 0]
def func(n):
    if n == 3:
        print(b)
        return

    # 해당 원소값을 추가하는 경우
    b[n] = 1
    func(n+1)
    b[n] = 0
    # 해당 원소를 추가하지 않는 경우
    func(n+1)

# 모든 부분집합 원소의 합
def subsum(n, k, val):
    if n == k:
        print(val)
        return

    subsum(n+1, k, val+A[n])
    subsum(n+1, k, val)

subsum(0, 3, 0)

# 서로다른 K개의 자연수를 집합에서 부분집합 원소의 합이 M인 경우의 수

def f(n, k, sum, M):
    global cnt
    if sum == M:
        cnt += 1
        return
    elif n == k:
        return
    else:
        f(n+1, k, sum+A[n], M)
        f(n+1, k, sum, M)