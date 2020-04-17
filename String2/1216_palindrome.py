# 1216. [S/W 문제해결 기본] 3일차 - 회문2
import sys
sys.stdin = open('1216.txt', 'r')

# def Pal(arr):

#     for case in range(100, 0, -1):
#         for row in range(len(arr)):
#             for col in range(len(arr[0])):
#                 # 열 슬라이딩
#                 if col <= (len(arr) - case):
#                     for i in range(case >> 1):
#                         if arr[row][col+i] != arr[row][col+case-1-i]:
#                             break
#                     else:
#                         return case
#                 # 행 슬라이딩
#                 if row <= (len(arr) - case):
#                     for i in range(case >> 1):
#                         if arr[row+i][col] != arr[row+case-1-i][col]:
#                             break
#                     else:
#                         return case
#     return 1

# for _ in range(10):
#     T = input()
#     arr = []
#     for _ in range(100):
#         arr.append(list(input()))
#     print('#{} {}'.format(T, Pal(arr)))





for tc in range(1, 11):
    N = int(input())   # 회문 길이
    arr = [input() for _ in range(100)]

    ans = 1             # 지금까지 찾은 최대 길이
    # 행/열에 대해서
    for idx in range(100):
        for s in range(100):
            for e in range(99, s, -1):
                L = e - s + 1
                if L <= ans: break
                for i in range(L//2):
                    if arr[idx][s + i] != arr[idx][e - i]: break
                else:
                    ans += 1
                if L <= ans: break
                for i in range(L//2):
                    if arr[s + i][idx] != arr[e - i][idx]: break
                else:
                    ans = L
    print(ans)



# 홀수/짝수 길이를 이용하는 방법
for tc in range(1, 11):
    N = int(input())   # 회문 길이
    arr = [input() for _ in range(8)]

    ans = 1             # 지금까지 찾은 최대 길이
    # 행/열에 대해서
    for idx in range(100):
        for x in range(100):   # x: 기준위치
            # 길이가 짝수
            # 행에 대해서
            l, r, cnt = x, x+1, 0
            while l >= 0 and r <100:
                if arr[idx][l] != arr[idx][r]: break
                l, r, cnt = l-1, r+1, cnt + 2
            ans = max(ans, cnt)

            # 열에 대해서
            l, r, cnt = x, x+1, 0
            while l >= 0 and r <100:
                if arr[l][idx] != arr[r][idx]: break
                l, r, cnt = l-1, r+1, cnt + 2
            ans = max(ans, cnt)

            # 길이가 홀수
            # 행에 대해서
            l, r, cnt = x-1, x+1, 1
            while l >= 0 and r <100:
                if arr[idx][l] != arr[idx][r]: break
                l, r, cnt = l-1, r+1, cnt + 2
            ans = max(ans, cnt)

            # 열에 대해서
            l, r, cnt = x-1, x+1, 1
            while l >= 0 and r <100:
                if arr[l][idx] != arr[r][idx]: break
                l, r, cnt = l-1, r+1, cnt + 2
            ans = max(ans, cnt)
            
    print(ans)