# 4828. [파이썬 S/W 문제해결 기본] 1일차 - min max

def my_minmax(my_list): # 최대값과 최소값의 차이를 구하는 함수
    my_min = my_list[0]
    my_max = my_list[0]

    for i in range(len(my_list)):
        if my_min > my_list[i]:
            my_min = my_list[i]
        if my_max < my_list[i]:
            my_max = my_list[i]
    return my_max - my_min

T = int(input())
# K = input()
# print(K)
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    numbers = list(map(int, input().split()))
    print('#{} {}'.format(test_case, my_minmax(numbers)))
