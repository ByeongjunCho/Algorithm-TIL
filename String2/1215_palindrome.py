# import sys
# sys.stdin(open('input.txt', 'r'))
# def Pal(arr, M):
#     # 행
#     count = 0
#     for row in range(len(arr)):
#         for col in range(len(arr[0])-M+1):
#             for i in range(M >> 1):
#                 if arr[row][col+i] != arr[row][col+M-1-i]:
#                     break
#             else:
#                 count += 1
#     for row in range(len(arr)-M+1):
#         for col in range(len(arr[0])):
#             for i in range(M >> 1):
#                 if arr[row+i][col] != arr[row+M-1-i][col]:
#                     break
#             else:
#                 count += 1
#     return count

# for T in range(1, 11):
#     M = int(input())
#     arr = []
#     for _ in range(8):
#         arr.append(list(input()))
#     print('#{} {}'.format(T, Pal(arr, M)))


# 전체 문자열 N = 10, 찾을 회문의 길이 M = 7 => N-M+1개의 문자열
# 길이가 M인 구간의 시작과 끝
# Start = (0~N-M)
# END = Start+M-1

for tc in range(1, 11):
    N = int(input())   # 회문 길이
    arr = [input() for _ in range(8)]
    ans = 0
    # 한행에 대해서
    for idx in range(8):
        for s in range(8 - N + 1):
            e = s + N -1
            for i in range(N//2):
                if arr[idx][s + i] != arr[idx][e - i]: break
            else:
                ans += 1
            for i in range(N//2):
                if arr[s + i][idx] != arr[e - i][idx]: break
            else:
                ans += 1

        