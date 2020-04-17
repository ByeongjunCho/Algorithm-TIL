# 백준 17471 게리맨더링
from collections import deque

N = int(input())
peoples = [0] + list(map(int, input().split()))
G = [[] for _ in range(N+1)]
for i in range(1, N+1):
    index = list(map(int, input().split()))
    for j in range(1, len(index)):
        G[i].append(index[j])

def isConnect(vec):
    # 모든 노드가 연결되었는지 확인
    if len(vec) == 1:
        return True
    q = deque()
    count = 1
    visit = [0] * (N+1)
    visit[vec[0]] = 1
    q.append(vec[0])
    while q:
        v = q.popleft()
        for u in G[v]:
            if u in vec and not visit[u]:
                visit[u] = 1
                count += 1
                q.append(u)
    if count == len(vec):
        return True
    else:
        return False


vector = set(range(1, N+1))
def comb(start, end):
    if len(s) == end:
        vec1 = set(s)
        vec2 = vector - vec1
        # 선거구가 연결되어 있는지 확인하여
        if isConnect(list(vec1)) and isConnect(list(vec2)):
            # 인구수를 더함
            p1, p2 = 0, 0
            for i in vec1:
                p1 += peoples[i]
            for j in vec2:
                p2 += peoples[j]
            global myMin
            myMin = min(myMin, abs(p1-p2))
        return

    for i in range(start, N+1):
        s.append(i)
        comb(i+1, end)
        s.pop()

myMin = 0xffffff
for cnt in range(1, N):
    s = []
    comb(1, cnt)
if myMin == 0xffffff:
    print(-1)
else:
    print(myMin)