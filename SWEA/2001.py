# 파리 퇴치

# arr = [[1, 3, 3, 6, 7],[8, 13, 9, 12, 8],[4, 16, 11, 12, 6],
# [2, 4, 1, 23, 2],[9, 13, 4, 7, 3]]

# window = [[1, 1],[1, 1]]


# def conv_max(tar, win): # 입력이 2중 리스트라 가정
#     tar_w, tar_h = len(tar[0]), len(tar) # target의 width와 height
#     win_w, win_h = len(win[0]), len(win) # window의 width와 height

#     slide_w = tar_w - win_w + 1 # 슬라이딩 width
#     slide_h = tar_h - win_h + 1 # 슬라이딩 height
     
#     aa = []
#     for h in range(slide_h):  
#         for w in range(slide_w):
#             result = 0
#             for j in range(win_h):
#                for i in range(win_w):
#                    result += win[j][i] * tar[h+j][w+i]


#             else:
#                 aa.append(result)
#     return aa
# print(len(conv_max(arr, window)))



def conv_max(tar, tar_size, win_size): # 입력이 2중 리스트라 가정
    
    slide_w = tar_size - win_size + 1 # 슬라이딩 width
    slide_h = tar_size - win_size + 1 # 슬라이딩 height
     
    fly_max = 0
    for h in range(slide_h):  
        for w in range(slide_w):
            result = 0
            for j in range(win_size): # row
                for i in range(win_size): # column
                    # result += win[j][i] * tar[h+j][w+i]
                    result += tar[h+j][w+i]

            fly_max = result if fly_max < result else fly_max
            
    return fly_max


test_case = int(input())

for case in range(1, test_case + 1):
    test_arr = []
    target_size, window_size = map(int, input().split(' '))
    for _ in range(target_size):
        test_arr.append(list(map(int, input().split(' '))))
    
    print(f'#{case} {conv_max(test_arr, target_size, window_size)}')