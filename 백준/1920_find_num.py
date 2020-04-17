def binary_search(arr, key):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start+end)>>1
        
        if arr[mid] == key:
            return 1
        elif arr[mid] > key:
            end = mid-1
        else:
            start = mid+1
    return 0
N = int(input())
arr_N = list(map(int, input().split()))
arr_N.sort()
M = int(input())
arr_M = list(map(int, input().split()))

for key in arr_M:
    print(binary_search(arr_N, key))