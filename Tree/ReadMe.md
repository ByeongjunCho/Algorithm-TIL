# Tree 구조

## 1. Tree 구현

* 연결리스트를 이용한 구현
* 배열을 이용한 구현

## 2. 서로소 집합

* 서로 중복되는 원소가 없는 집합(교집합이 없는 집합을 만든다.)
* 집합에 속한 멤버 중 하나를 대표자로 하여 집합을 구분한다.

## 3. 연산 효율 증가방법

* 랭크가 낮은 집합을 랭크가 높은 집합에 붙인다.
* 원소의 루트를 찾고, 루트를 부모로 변경한다.

## 4. 최소신장트리

* 무향 가중치 그래프에서 신장 트리를 구성하는 간선들의 가중치의 합이 최소인 신장 트리

### 1. 크루스칼 알고리즘

1. 모든 간선을 가중치에 따라 오름차순 정렬
2. 가중치가 낮은 간선부터 선택하면서 트리를 증가시킴
   - 사이클이 존재하면 다음으로 가중치가 낮은 간선 선택
3. N-1개의 간선이 선택될 때까지 2를 반복

### 2. Prim 알고리즘

* 하나의 정점에서 연결된 간선들 중에 하나씩 선택하면서 MST를 만들어가는 방식

1. 임의 정점을 하나 선택해서 시작
2. 선택한 정점과 인접하는 정점들 중의 최소 비용의 간선이 존재하는 정점을 선택
3. 모든 정점이 선택될 때가지 1, 2과정을 반복

## 4. 다익스트라 알고리즘

S -> U -> V와 S->V 경로가 있을 때 최소경로는 min(D[S->V], D[S->U] + D[U->V])가 될 것이다.

1. BFS와 간선 완화를 이용한 방법

```python
# BFS + 간선 완화를 이용한 방법
def BFS(s):
    D = [0xffffff] * (V + 1) # D[] 초기값 설정
    # visit = [False] * (V + 1)
    Q = deque()
    Q.append(s);
    D[s] = 0

    while Q:
        u = Q.popleft()
        for v, w in G[u]:
            # v정점까지의 최소값 > 현재 정점(u) 최소값 + 가중치 
            if D[v] > D[u] + w: # u -> v
                D[v] += D[u] + w
                Q.append(v)
```

2. Dijstra 알고리즘

```python
def DIJKSTRA_ARRAY(s):

    D = [0xfffff] * (V + 1)
    P = [i for i in range(V + 1)]
    visit = [False] * (V + 1)
    D[s] = 0

    cnt = V
    while cnt:                              # 정점의 수 만큼 반복

        u, MIN = 0, 0xfffff                 # D[] 가 최소인 정점 찾기
        for i in range(1, V + 1):           # 무식하게 리스트에서 찾기
            if not visit[i] and D[i] < MIN:
                u, MIN = i, D[i]

        visit[u] = True

        for v, w in G[u]:
            if not visit[v] and D[v] > D[u] + w:
                D[v] = D[u] + w
                P[v] = u

        cnt -= 1

    print(D[1: V + 1])
    print(P[1: V + 1])


V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]
for i in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w))
    G[v].append((u, w))

DIJKSTRA_ARRAY(1)
```

