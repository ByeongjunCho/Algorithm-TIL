# 구간 합

    target_size, window_size = list(map(int, input().split()))
    target_list = list(map(int, input().split()))
    window_list = [1] * window_size

    max_val = 1e-10
    min_val = 1e10

    slide_size = target_size - window_size + 1

    for tar in range(slide_size):
        result = 0
        for win in range(window_size):
            result += target_list[tar+win] * window_list[win]
        # 큰것과 작은것을 얻기 위해 비교를 한다.
        max_val = result if result > max_val else max_val
        min_val = result if result < min_val else min_val

    print(f'# {max_val-min_val}')