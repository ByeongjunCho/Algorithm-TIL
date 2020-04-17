# 스도쿠 검증

def check_sudoku(tar): # 2차원 리스트 입력
    slide = [0, 3, 6]
    
    # 슬라이딩 3의 convolution 구현
    for slide_h in slide:
        for slide_w in slide:
            result = []
            for win_h in range(3):
                for win_w in range(3):
                    result.append(tar[slide_h+win_h][slide_w+win_w])
            if len(set(result)) != 9:
                return 0

    for row in range(9):
        result = []
        for col in range(9):
            result.append(tar[row][col])
        if len(set(result)) != 9:
            return 0
    for col in range(9):
        result = []
        for row in range(9):
            result.append(tar[row][col])
        if len(set(result)) != 9:
            return 0
    return 1

case = int(input())

for T in range(case):
    test_list = []
    for _ in range(9):
        tmp = list(map(int, input().split()))
        test_list.append(tmp)
    print(f'#{T+1} {check_sudoku(test_list)}')