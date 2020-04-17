# 재귀 호출
# 1. 재귀적으로 문제를 해결
#     - 재귀적 정의를 코드 구현할 때 사용
#     - 좀 더 작은 문제의 해를 이용해서 좀 더 큰 문제의 해를 구하는 방법
#     -> 분할정복, DP
# 2. 그래프 탐색, DFS, 트리 순회
# 3. 백트래킹(상태 공간 트리 탐색)

# for, while를 사용하지 않고 반복


cnt = 0
bit = [0] * 3
def printHello(i, n):
    global cnt
    if i == n:
        cnt += 1
        print(bit)
        return
    else:
        # print(i, 'Hello')
        bit[i] = 1
        printHello(i + 1, n)
        bit[i] = 0
        printHello(i + 1, n)
        # print(i, 'Hello')

printHello(0, 3)
print('cnt = ', cnt)

