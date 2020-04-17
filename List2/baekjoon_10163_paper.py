# 백준 10163 색종이

arr = [[0 for _ in range(101)] for _ in range(101)]

N = int(input())
for T in range(1, N+1):
    x, y, dx, dy = map(int, input().split())
    for i in range(x, x + dx):
        for j in range(y, y + dy):
            arr[i][j] = T

for i in range(1, N+1):
    count = 0
    for j in range(len(arr)):
        count += arr[j].count(i)

    # for j in arr:
    #     count += j.count(i)
    print(count)

