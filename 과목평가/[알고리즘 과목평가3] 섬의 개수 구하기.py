# [알고리즘 과목평가3] 섬의 개수 구하기
tmp = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 0], [0, 1], [1, -1], [1, 0], [1, 1]]

def island(arr, visit, N):
    count = 0
    for row in range(N):
        for col in range(N):
            if arr[row][col] > 0 and not visit[row][col]:
                S = [[row, col]]
                count += 1
                while S:
                    for i, j in tmp:
                        if row + i < 0 or row + i > N-1 or col + j < 0 or col + j > N-1:
                            continue

                        if arr[row+i][col+j] and not visit[row+i][col+j]:
                            S.append([row, col])
                            row = row+i
                            col = col+j
                            visit[row][col] = 1
                            # print(S)
                            S.append([row, col])
                            break
                    else:
                        row, col = S.pop()
    return count



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0 for _ in range(N)] for _ in range(N)]

    print('#{} {}'.format(tc, island(arr, visit, N)))
