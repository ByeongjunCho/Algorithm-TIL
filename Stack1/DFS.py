import sys
sys.stdin = open('DFS_input.txt', 'r')


def DFS(v):
    # 시작점을 방문하고, 스택에 push
    S = []
    visit[v] = True; print(v, end=' ')
    S.append(v)
    while S:   # 빈 스택이 아닐동안 반복
        for w in G[v]:
            if not visit[w]:    # v의 방문하지 않은 인접정점 w를 찾아서
                visit[w] = True; print(w, end = ' ')
                S.append(v)     # w를 방문하고, v를 스택에 push
                v = w       # v를 w로 설정
                break
        else:   # 인접정점이 없다면, 스택에서 pop()하여
            v = S.pop()  # v로 설정


def DFS(v):
    visit[v] = True; print(v, end=' ')

    for w in G[v]:
        if not visit[w]:
            DFS(w)



V, E = map(int, input().split()) # 정점수, 간선수
G = [[] for _ in range(V + 1)] # 1~V까지 사용, 0번은 사용하지 않음
visit = [False] * (V + 1)   # 방문정보

for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)   # 무향 그래프

# for i in range(1, V + 1):
#     print(i, '-->', G[i])
DFS(1)
