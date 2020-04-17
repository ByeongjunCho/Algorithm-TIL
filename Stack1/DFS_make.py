import sys
sys.stdin = open('DFS_input.txt', 'r')

V, E = map(int, input().split())  # 정점, 간선
Graph = [[] for _ in range(V+1)]
visit = [False] * (V+1)

for _ in range(V):
    u, v = map(int, input().split())
    # 완전연결 그래프이므로
    Graph[u].append(v)
    Graph[v].append(u)

print(Graph)

def dfs(v):
    S = [v]
    visit[v] = True

    while S:
        for w in Graph[v]:
            if not visit[w]:
                visit[w] = True
                print('{}-->{}'.format(v, w))
                S.append(w)
                v = w
                break
        else:
            v = S.pop()
            print('{}-->{}'.format(v, w))
        # print(S)



visit = [False] * (V+1)
def dfs(v):
    visit[v] = True; print(v, end=' ')
    
    for w in Graph[v]:
        if not visit[w]:
            dfs(w)
            
print(dfs(1))