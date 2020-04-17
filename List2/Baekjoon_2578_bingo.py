def my_arrsum(arr):
    '''
    각 행과 열, 대각선의 합을 가진 리스트를 반환하는 함수
    순서는 행의 합, 열의 합, /\순서로 반환.
    '''
    tmp1 = 0 # /
    tmp2 = 0 # \
    tmp_col = [0] * 5
    tmp_row = []

    for row in range(len(arr)):
        result =0
        for col in range(len(arr[0])):
            result += arr[row][col]
            tmp_col[col] += arr[row][col]
            if row == col:
                tmp1 += arr[row][col]
            if row+col == 4:
                tmp2 += arr[row][col]
        tmp_row.append(result)
    return tmp_row + tmp_col + [tmp1] + [tmp2]

def bingo(target_arr, bingo_arr, sum_arr):
    target_tmp = []

    for i in range(len(target_arr)):
        target_tmp.extend(target_arr[i])
    count = 0
    for row in range(len(bingo_arr)):
        for col in range(len(bingo_arr[0])):
            tmp_idx = target_tmp.index(bingo_arr[row][col])
            i,j = tmp_idx // len(bingo_arr), tmp_idx % len(bingo_arr[0])
            sum_arr[i] -= bingo_arr[row][col]
            sum_arr[len(bingo_arr) + j] -= bingo_arr[row][col]
            if i == j:
                sum_arr[len(sum_arr)-2] -= bingo_arr[row][col]
            if i+j == 4:
                sum_arr[len(sum_arr)-1] -= bingo_arr[row][col]
            count += 1

            if sum_arr.count(0) >= 3:
                return count

test_arr = []
for _ in range(5):
    test_arr.append(list(map(int, input().split())))

bingo_arr = []
for _ in range(5):
    bingo_arr.append(list(map(int, input().split())))

bingo_sum = my_arrsum(test_arr)
print(bingo(test_arr, bingo_arr, bingo_sum))
