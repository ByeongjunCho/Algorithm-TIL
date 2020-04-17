# 어디에 단어가 들어갈 수 있을까
# def conv_count(tar, tar_size, dst): # 입력이 2중 리스트라 가정
#     count = 0
#     for height in range(tar_size):
#         result = 0
#         for width in range(tar_size):
#             result += tar[height][width]
#         if result == dst:
#             count += 1
    
#     for width in range(tar_size):
#         result = 0
#         for height in range(tar_size):
#             result += tar[width][height]
#         if result == dst:
#             count += 1
#     return count

# def conv_count(tar, tar_size, win_size): # 입력이 2중 리스트라

#     # 1. 1x3 convolution
#     win_width_size = win_size
#     win_height_size = 1
#     slide_w = tar_size - win_width_size + 1 # 슬라이딩 width
#     slide_h = tar_size - win_height_size + 1 # 슬라이딩 height
    


#     count =0

#     for h in range(slide_h):
#         result_line = 0  
#         for w in range(slide_w):
#             result = 0
#             for j in range(win_height_size):
#                 for i in range(win_width_size):
#                     # result += win[j][i] * tar[h+j][w+i]
#                     result += tar[h+j][w+i]
#             result_line += result if result == win_size else 0
            
#         if result_line == win_size:
#             count += 1
    
#     # 2. 3x1 convoultion
#     win_width_size = 1
#     win_height_size = win_size
#     slide_w = tar_size - win_width_size + 1 # 슬라이딩 width
#     slide_h = tar_size - win_height_size + 1 # 슬라이딩 height
    

#     for w in range(slide_w):
#         result_line = 0
#         for h in range(slide_h):
#             result = 0
#             for j in range(win_height_size):
#                 for i in range(win_width_size):
#                     result += tar[h+j][w+i]
#             result_line += result if result == win_size else 0
    
#         if result_line == win_size:
#             count += 1
#     return count


def conv_count(tar, tar_size, win_size): # 입력이 2중 리스트라

    # 1. 1x3 convolution
    win_width_size = win_size
    win_height_size = 1
    slide_w = tar_size - win_width_size + 1 # 슬라이딩 width
    slide_h = tar_size - win_height_size + 1 # 슬라이딩 height
    
    
    conv1 = []
    for h in range(slide_h):
        for w in range(slide_w):
            result = 0
            for j in range(win_height_size):
                for i in range(win_width_size):
                    # result += win[j][i] * tar[h+j][w+i]
                    result += tar[h+j][w+i]
            conv1.append(result)
    
    for h in range(slide_h): # 5
        print('')
        for w in range(slide_w): # 3
            print(conv1[slide_w * h + w], end=' ')

    # 2. 3x1 convoultion
    win_width_size = 1
    win_height_size = win_size
    slide_w = tar_size - win_width_size + 1 # 슬라이딩 width
    slide_h = tar_size - win_height_size + 1 # 슬라이딩 height
    
    conv2 = []
    for w in range(slide_w):
        for h in range(slide_h):
            result = 0
            for j in range(win_height_size):
                for i in range(win_width_size):
                    result += tar[h+j][w+i]
            conv2.append(result)
    for w in range(slide_w): # 5
        print('')
        for h in range(slide_h): # 3
            print(conv2[slide_h * w + h], end=' ')

test_case = int(input())

for case in range(1, test_case + 1):
    test_arr = []
    target_size, dst = map(int, input().split())
    for _ in range(target_size):
        test_arr.append(list(map(int, input().split())))
    
    print(f'#{case} {conv_count(test_arr, target_size, dst)}')

# 0 0 1 1 1
# 1 1 1 1 0
# 0 0 1 0 0
# 0 1 1 1 1
# 1 1 1 0 1
