def conv_count(tar, tar_size, win_size): # 입력이 2중 리스트라 가정
    
    row_result = []
    for height in range(tar_size):
        result = 0
        for width in range(tar_size):
            result += tar[height][width]
        row_result.append(result)
    
    col_result = []
    for width in range(tar_size):
        result = 0
        for height in range(tar_size):
            result += tar[width][height]
        col_result.append(result)

    # 1. 1x3 convolution
    win_width_size = win_size
    win_height_size = 1
    slide_w = tar_size - win_width_size + 1 # 슬라이딩 width
    slide_h = tar_size - win_height_size + 1 # 슬라이딩 height
    


    count =0

    for h in range(slide_h):  
        for w in range(slide_w):
            result = 0
            for j in range(win_height_size):
                for i in range(win_width_size):
                    # result += win[j][i] * tar[h+j][w+i]
                    result += tar[h+j][w+i]

            if result == win_size and win_size == row_result[h]:
                count += 1
    
    # 2. 3x1 convoultion
    win_width_size = 1
    win_height_size = win_size
    slide_w = tar_size - win_width_size + 1 # 슬라이딩 width
    slide_h = tar_size - win_height_size + 1 # 슬라이딩 height
     
    for h in range(slide_h):  
        for w in range(slide_w):
            result = 0
            for j in range(win_height_size): # row
                for i in range(win_width_size):
                    # result += win[j][i] * tar[h+j][w+i]
                    result += tar[h+j][w+i]

            if result == win_size and win_size == col_result[w]:
                count += 1
    return count


test_case = int(input())

for case in range(1, test_case + 1):
    test_arr = []
    target_size, window_size = map(int, input().split())
    for _ in range(target_size):
        test_arr.append(list(map(int, input().split())))
    
    print(f'#{case} {conv_count(test_arr, target_size, window_size)}')