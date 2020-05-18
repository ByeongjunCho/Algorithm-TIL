'''
boj 17136번-색종이 붙이기
backtracing을 이용한 풀이
'''

# 해당 색종이를 사용해도 되는지 판단하는 함수
def check(i, j, size):
    # 왼쪽 위 시작위치 좌표(i, j), 덮을 size
    if i+size > 10 or j+size > 10:
        return False

    for y in range(i, i+size):
        for x in range(j, j+size):
            if not matrix[y][x]:
                return False
    return True


# 색종이로 덮어서 원하는 숫자로 변환하는 함수
def mapTonum(i, j, size, num):  
    # 왼쪽 위 시작위치 좌표(i, j), 덮을 size
    for y in range(i, i+size):
        for x in range(j, j+size):
            matrix[y][x] = num

def back(i, j):
    if i>9:
        global result
        for y in range(10):
            for x in range(10):
                if matrix[y][x]:
                    return
        result = min(result, 25 - sum(paper))
        return

    if matrix[i][j]:    
        for size in range(5, 0, -1):
            if check(i, j, size):
                if paper[size]:
                    paper[size] -= 1
                    mapTonum(i, j, size, 0)

                    if j+size <= 9:
                        back(i, j+size)
                    else:
                        back(i+1, 0)
                    
                    paper[size] += 1
                    mapTonum(i, j, size, 1)
                else:
                    return
    else:
        if j+1 <= 9:
            back(i, j+1)
        else:
            back(i+1, 0)

                

# load matrix
matrix = [list(map(int, input().split())) for _ in range(10)]
paper = [0, 5, 5, 5, 5, 5]

result = 30

back(0, 0)
if result == 30:
    print(-1)
else:
    print(result)