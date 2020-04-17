# 4834. [파이썬 S/W 문제해결 기본] 1일차 - 숫자 카드
T = int(input())

def number_card(my_list):
    idx = 0
    max_num = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] >= max_num:
            idx = i
            max_num = my_list[i]
    return idx, max_num
for test_case in range(1, T + 1):
    # ///////////////////////////////
    N = int(input())
    card_number = list(map(int, list(input())))
    # 카드 숫자가 나온 횟수만큼 담는다.
    result = [0] * 10
    for i in card_number:
        result[i] += 1
    index, num = number_card(result)

    print('#{} {} {}'.format(test_case, index, num))