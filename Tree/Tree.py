# 트리
# - 싸이클이 없다:
# - 트리의 노드 수 n개, 간선 수 = n - 1개
# - 그래프의 관점 connected component(연결 컴포턴트)


# 최소 공통 조상(LCA)
# - Least Common Ancestor
# - Lowest Common Ancestor

# 13 12
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
import sys
sys.stdin = open('input.txt', 'r')
V, E = map(int, input().split())  # 노드수, 간선수
L = [0] * (V+1)     # tree = [[0,0,0] for _ in range(V+1)]
R = [0] * (V+1)     # tree = [[] for _ in range(V+1)]
P = [0] * (V + 1)

arr = list(map(int, input().split()))
for i in range(0, E*2, 2):
    p, c = arr[i], arr[i+1]
    if L[p] == 0:
        L[p] = c
    else:
        R[p] = c
    P[c] = p     # 부모 정보는 필요한 경우에 저장해서 사용

# 전위순회
def preorder(v):
    if v == 0:
        return
    print(v, end=' ')
    preorder(L[v])
    preorder(R[v])

# 중위순회
def inorder(v): # V = 현재노드
    if v == 0:
        return
    inorder(L[v])
    print(v, end=' ')
    inorder(R[v])

# 후위순회
def postorder(v):
    if v == 0:
        return
    postorder(L[v])
    postorder(R[v])
    print(v, end=' ')


print('----------전위순회----------')
preorder(1), print()
print('---------전위순회끝---------')

print('----------중위순회----------')
inorder(1), print()
print('---------중위순회끝---------')

print('----------후위순회----------')
postorder(1), print()
print('---------후위순회끝---------')


height = 0
def treeHeight(v, k): # v를 루트로 하는 트리의 높이
    if v == 0:
        global height
        height = max(height, k-1)
        return
    treeHeight(L[v], k+1)
    treeHeight(R[v], k+1)

treeHeight(1, 0)
print(height)


node = 0
def treeSize(v): # v를 루트로 하는 트리의 노드 수 계산
    global node
    if v == 0:
        node -= 1
        return
    treeSize(L[v])
    node += 1
    treeSize(R[v])
    node += 1

treeSize(3)
print(node)


def myGrand(v, g):
    if P[v] == 0:
        # print(v)
        return
    myGrand(P[v], g)
    g.append(P[v])

g1 = []
g2 = []
myGrand(9, g1)
myGrand(13, g2)

print(g1)
print(g2)
ugrand = []
for i in range(len(g1)-1, -1, -1):
    for j in range(len(g2)-1, -1, -1):
        if g1[i] == g2[j]:
            ugrand.append(g1[i])
            break
print(ugrand)
# ------------------
