def conv(arr, arr_row_size, arr_col_size, window_size):
    row_slide = arr_row_size - window_size + 1
    col_slide = arr_col_size - window_size + 1

    max_result = 0  # 최대값
    for row in range(row_slide):
        for col in range(col_slide):
            result = 0
            for win_row in range(window_size):
                for win_col in range(window_size):
                    if win_row + row == row or win_row + row == row+window_size -1:
                        # 맨 위의 행과 마지막 행을 선택
                        result += arr[row+win_row][col+win_col]
                    else:
                        # 맨위의 행과 마지막 행이 아니라면
                        if win_col+col == col or win_col + col == col+window_size - 1:
                            # 맨 앞의 열과 맨 뒤의 열이면 값을 더해준다.
                            result += arr[row+win_row][col+win_col]
            if result > max_result:
                max_result = result
    return max_result


T = int(input())
for tc in range(1, 1+T):
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print('#{} {}'.format(tc, conv(arr, N, M, K)))