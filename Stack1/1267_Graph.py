# 1267. [S/W 문제해결 응용] 10일차 - 작업순서
import sys
sys.stdin = open('1267_input.txt', 'r')

# 위상 정렬
# 방법 1. 진입 차수가 0인 정점을 큐에 삽입
# 방법 2. DFS를 수행하면서 더이상 갈 곳이 없으면 그 자리를 기록하고 역순으로 출력


def DFS(v):
    visit[v] = True
    for w in G[v]:
        if not visit[w]:
            DFS(w)
    stack.append(w)

for tc in range(1, 11):
    V, E = map(int, input().split())
    G = [[] for _ in range(V+1)]
    start_case = set(range(1, V+1)) # 시작값
    input_count = [0] * (V+1) # 각 노드에 들어오는 엣지 수
    caseE = list(map(int, input().split()))

    for i in range(E):
        G[caseE[i << 1]].append(caseE[(i << 1)+1])
        start_case -= {caseE[(i << 1)+1]}
        input_count[caseE[(i << 1)+1]] += 1
    visit = [0] * (V+1)

    v = start_case.pop()
    visit[v] = 1
    S = [v]
    result = [str(v)]
    while S or start_case:
        if not S:
            v = start_case.pop()
            result.append(str(v))
            visit[v] = 1
            S = [v]

        for i in range(len(G[v])):
            w = G[v][i]
            if visit[w] + 1 == input_count[w] and w:
                # if str(w) not in result:
                #     result.append(str(w))
                result.append(str(w))
                visit[w] += 1
                S.append(v)
                v = w
                break
            elif visit[w]+1 != input_count[w] and input_count[w] > 1 and w:
                visit[w] += 1
                G[v][i] = 0
        else:
            v = S.pop()

    print('#{} {}'.format(tc, ' '.join(result)))
    print(len(result))





