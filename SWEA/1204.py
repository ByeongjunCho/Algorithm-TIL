# 최빈수 구하기
def check_degree(degree_list):
    tmp_list = [0] * 101
    for degree in degree_list:
        tmp_list[degree] += 1

    # 뒤집는다.
    tmp_list = list(reversed(tmp_list))
    return 100 - tmp_list.index(max(tmp_list))

test_case = int(input())
for _ in range(1, test_case+1):
    test_num = int(input())
    degree_list = list(map(int, input().split()))
    print(f'#{test_num} {check_degree(degree_list)}')