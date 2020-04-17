# 2105. [모의 SW 역량테스트] 디저트 카페

def tour(r, c, left, right):  # 왼쪽 길이, 오른쪽 길이
    # if r+left < 0 or c-left < 0 or r+left+right > N or c-left+right > N:
    #         return

    row = r
    col = c
    s = [0] * 101
    try:
        # 왼쪽 아래 방향
        for _ in range(left):
            row, col = row+1, col-1
            if 0 <= row < N and 0 <= col < N and not s[arr[row][col]]:
                s[arr[row][col]] = 1
            else:
                return
        # 오른쪽 아래 방향
        for _ in range(1, right+1):
            row, col = row + 1, col + 1
            if 0 <= row < N and 0 <= col < N and not s[arr[row][col]]:
                s[arr[row][col]] = 1
            else:
                return
        # 오른쪽 위
        for _ in range(1, left+1):
            row, col = row - 1, col + 1
            if 0 <= row < N and 0 <= col < N and not s[arr[row][col]]:
                s[arr[row][col]] = 1
            else:
                return
        # 왼쪽 위
        for _ in range(1, right+1):
            row, col = row - 1, col - 1
            if 0 <= row < N and 0 <= col < N and not s[arr[row][col]]:
                s[arr[row][col]] = 1
            else:
                return

        for i in range(len(s)):
            if s[i]:
                print(i)
        print(r,c,left, right)
        return True
    except:
        return False


def maxtour():
    K = N - 1
    while K > 2:
        for r in range(N):
            for c in range(N):
                for i in range(1, K):
                    if tour(r, c, i, K-i):
                        return K*2
        K -= 1

    return -1



for tc in range(1, 1+int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]


    tour(0, 1, 1, 1)