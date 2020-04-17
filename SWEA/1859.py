# 백만장자 프로젝트
test_case = int(input())
# test_case = 1
# N = '5'
# price = '10 7 6'
# price = '1 1 3 1 2'


for case in range(test_case):
    N = input()
    # price = list(map(int, price.split()))
    price = list(map(int, input().split()))
    len_price = len(price)

    loc = 0  # 위치변수
    get_price = 0  # 이득
    while True:
        # 1. 가장 큰 값이 있는 인덱스를 찾는다.
        if loc == len_price or loc == len_price - 1: 
            break
        # max_index = find_max_index(price)
        max_index = price.index(max(price))

        # 2. 인덱스 값이 현재 저장된 loc와 같은지 확인해서 같다면 다음부터 다시 시작한다..
        
        if max_index == loc:
            loc += 1
        else:
            get_price += max_index * price[:max_index + 1][-1] - sum(price[:max_index])
            loc += max_index + 1
        price = price[loc:]
        
    print(f'#{case + 1} {max(get_price, 0)}')