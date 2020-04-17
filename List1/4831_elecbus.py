# 4831. [파이썬 S/W 문제해결 기본] 1일차 - 전기버스

def max_list(my_list, num): # num보다 작거나 같은 리스트를 반환하는 함수
    result = []
    for i in range(len(my_list)):
        if my_list[i] <= num:
            result.append(my_list[i])
        else:
            break
    return result


T = int(input())  # 노선 수
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    # K:최대 이동 가능한 정류장 수, N:종점, M:충전기 설치 수
    elec_supply = list(map(int, input().split())) # 충전기 위치
    bus_loc = 0  # 현재 버스의 위치
    sup_num = 0  # 버스 충전소 충전 카운트
    tmp_len = 0
    while True:
        # 버스를 K만큼 이동한다
        bus_loc += K
        # 버스가 정류장 범위를 넘어가면 while문을 끝낸다
        if bus_loc >= N:
            break

        # 버스의 위치보다 작거나 같은 버스정류장 위치의 최대값을 얻는다.
        # 버스정류장이 없다면, 0을 반환하고 while문을 끝낸다.
        tmp_list = max_list(elec_supply, bus_loc)
        if tmp_list:
            bus_loc = tmp_list[-1]
            sup_num += 1
        else:
            sup_num = 0
            break
        if tmp_len == len(tmp_list):
            sup_num = 0
            break
        tmp_len = len(tmp_list)
    print('#{} {}'.format(test_case, sup_num))

