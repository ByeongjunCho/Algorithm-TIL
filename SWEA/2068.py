t_case = int(input())


for i in range(1, 1+t_case):
    case = list(map(int, input().split(' ')))
    print(f'#{i} {max(case)}')