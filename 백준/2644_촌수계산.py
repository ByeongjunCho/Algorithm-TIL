# 백준 2644번 - 촌수계산


# 그래프로 풀면 될꺼같음 아마도?


n = int(input())

fam = [x for x in range(n+1)]  # 조상이 같은지 확인하는 함수
tar1, tar2 = map(int, input().split())
for _ in range(int(input())):
    x, y = map(int, input().split())
    fam[y] = x


# 촌수 계산 함수
def root(tar, mat):
    mat.append(tar)
    if fam[tar] == tar:
        return tar
    return root(fam[tar], mat)

# 조상을 찾음
mat1 = []
tar1_p = root(tar1, mat1)
mat2 = []
tar2_p = root(tar2, mat2)


size = min(len(mat1), len(mat2))
if tar1_p == tar2_p:
    # 조상이 같다면 친척일 것이다
    for i in range(-1, -size-1, -1):
        if mat1[i] != mat2[i]:
            break
    if mat1[-size] == mat2[-size]:
        i = -size-1
    print(len(mat1[:i+1]) + len(mat2[:i+1]))
else:
    print(-1)
