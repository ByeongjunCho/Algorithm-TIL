# 4835. [파이썬 S/W 문제해결 기본] 1일차 - 구간합
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

def conv(list_case, window_size):
    slide_size = len(list_case) - window_size + 1
    for i in range(slide_size):
        for j in range(window_size):
            pass

for test_case in range(1, T + 1):
    # ///////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    target_size, window_size = list(map(int, input().split()))
    target_list = list(map(int, input().split()))
    window_list = [1] * window_size

    # 초기 비교를 위한 값
    max_val = 0
    min_val = 1e10

    slide_size = target_size - window_size + 1  # sliding거리

    for tar in range(slide_size):

        result = 0
        for win in range(window_size):
            result += target_list[tar+win] * window_list[win]
        # 큰것과 작은것을 얻기 위해 비교를 한다.
        if result > max_val:
            max_val = result

        if result < min_val:
            min_val = result

    print('#{} {}'.format(test_case, max_val-min_val))