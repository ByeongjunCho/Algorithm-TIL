# 4861. [파이썬 S/W 문제해결 기본] 3일차 - 회문


def Pal(arr, M, slide):

    result = ''
    # 행
    for row in range(M):
        for col in range(slide):
            for i in range(M >> 1):
                if arr[row][col+i] != arr[row][col+M-1-i]:
                    break
            else:
                for j in range(M):
                    result += arr[row][col+j]
                return result

    # 열
    for row in range(slide):
        for col in range(M):
            for i in range(M >> 1):
                if arr[row+i][col] != arr[row+M-1-i][col]:
                    break
            else:
                for j in range(M):
                    result += arr[row+j][col]
                return result


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    slide = N-M+1
    arr = []
    for _ in range(N):
        arr.append(list(input()))

    print('#{} {}'.format(test_case, Pal(arr, M, slide)))



