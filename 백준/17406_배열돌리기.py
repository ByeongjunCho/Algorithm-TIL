'''
백준-17406번 배열 돌리기4
시뮬레이션
'''
from copy import deepcopy

def perm(k):
    if k == len(play):
        copymat = deepcopy(mat)
        for r,c,s in play:
            while s:
                rotate(r, c, s, copymat)
                s -= 1
        global result
        result = min(result, min([sum(x) for x in copymat]))
        return

    for i in range(k, len(play)):
        play[i], play[k] = play[k], play[i]
        perm(k+1)
        play[k], play[i] = play[i], play[k]

def rotate(r, c, s, mat):
    left_top = (r-s-1, c-s-1)
    right_bottom = (r+s-1, c+s-1)

    cur_r = r-s-1
    cur_c = c-s-1
    tmp = mat[cur_r][cur_c]
    while cur_c != right_bottom[1]:
        tmp1 = mat[cur_r][cur_c+1]
        mat[cur_r][cur_c+1] = tmp
        tmp = tmp1
        cur_c += 1

    while cur_r != right_bottom[0]:
        tmp1 = mat[cur_r+1][cur_c]
        mat[cur_r+1][cur_c] = tmp
        tmp = tmp1
        cur_r += 1

    while cur_c != left_top[1]:
        tmp1 = mat[cur_r][cur_c-1]
        mat[cur_r][cur_c-1] = tmp
        tmp = tmp1
        cur_c -= 1

    while cur_r != left_top[0]:
        tmp1 = mat[cur_r - 1][cur_c]
        mat[cur_r - 1][cur_c] = tmp
        tmp = tmp1
        cur_r -= 1



# 배열의 크기(N, M), 회전 연산의 개수 K
N, M, K = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]
play = [list(map(int, input().split())) for _ in range(K)]

result = 0xffffff
perm(0)


print(result)