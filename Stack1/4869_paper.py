# 4869. [파이썬 S/W 문제해결 기본] 4일차 - 종이붙이기



# 길이 N이 만들어진 상태라면,
# 1. n-1을 만들고, 1x2의 사각형 붙이기
# 2. N-1 (2x1)*2 혹은 2x2
def paper(x, N):
    if x == N:
        return 1
    elif x > N:
        return 0
    else:
        return paper(x+10, N) + paper(x+20, N)*2

# def paper(x, N):
#     if x ==
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print('#{} {}'.format(tc, paper(0, N)))