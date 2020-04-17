import random

arr = [[9, 20, 2, 18, 11],
[19, 1, 25, 3, 21],
[8, 24, 10, 17, 7],
[15, 4, 16, 5, 6],
[12, 13, 22, 23, 14]]

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

result = 0 # 결과
for row in range(len(arr)):
    for col in range(len(arr[0])):
        for i in range(len(drow)):
            trow = row + drow[i]
            tcol = col + dcol[i]
            if trow < 0 or tcol < 0 or trow > len(arr)-1 or tcol > len(arr[0])-1:
                continue
            tmp = arr[trow][tcol] - arr[row][col]
            result += tmp if tmp > 0 else -tmp

print(result)


