# t_case = int('1')
# case = '3 17 1 39 8 41 2 32 99 2'
# case = '22 8 5 123 7 2 63 7 3 46'
# case3 = '6 63 2 3 58 76 21 33 8 1'

t_case = int(input())

for i in range(1, t_case+1):
    case_sum = 0
    # case = input()
    case = list(map(int, case.split()))
    for num in case:
        if num % 2:
            case_sum += num
        else:
            continue
    print(f'#{i} {case_sum}')

    