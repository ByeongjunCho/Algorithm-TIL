arr = [64, 25, 10, 22, 11]
n = len(arr)
# 첫번째 단계 [0, n-1]

for i in range(n-1):
    minIdx = i
    for j in range(minIdx+1, n):
        if arr[minIdx] > arr[j]:
            minIdx = j
    arr[i], arr[minIdx] = arr[minIdx], arr[i]

print(arr)



print(arr)