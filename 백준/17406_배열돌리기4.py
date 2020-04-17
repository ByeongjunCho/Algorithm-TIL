N, M, K = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

def square(r, c, s):
    stats = 1
    sr, sc = r-s-1, c-s-1
    er, ec = r+s-1, c+s-1
    tmp_r, tmp_c = sr, sc
    tmpb = arr[sr][sc]

    while tmp_c <= ec:
        tmp_c += 1
        tmpa = arr[tmp_r][tmp_c]
        arr[tmp_r][tmp_c] = tmpb
        tmpb = tmpa



for i in range(K):
    r, c, s = map(int, input().split())
