# Baekjoon 10815. 숫자 카드

# sangen_N = int(input())
# sangen_card = list(map(int, input().split()))
# test_N = int(input())
# test_card = list(map(int, input().split()))
# sangen_card.sort()
#
#
# def binary_sort(arr, num):
#
#     if arr[0] > num or arr[-1] < num :
#         return '0'
#
#     start = 0
#     end = len(arr)-1
#     while start <= end:
#         mid = (start+end) >> 1
#         if arr[mid] == num:
#             return '1'
#         elif arr[mid] > num:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return '0'
#
# for i in range(test_N):
#     print(binary_sort(sangen_card, test_card[i]), end=' ')


sangen_N = input()
sangen_card = set(input().split()) # 이진탐색트리, 해싱
test_N = input()
test_card = input().split()

for i in test_card:
    if i in sangen_card:
        print(1, end=' ')

    else:
        print(0, end=' ')

# sangen_N = int(input())
# sangen_card = list(map(int, input().split()))
# test_N = int(input())
# test_card = list(map(int, input().split()))
#
# for i in range(test_N):
#     result[i] = binary_sort(sangen_card, test_card[i])
