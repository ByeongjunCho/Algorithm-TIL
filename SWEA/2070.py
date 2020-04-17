t_case = int(input())


for i in range(1, 1+t_case):
    case = list(map(int, input().split(' ')))
    if case[0] > case[1]:
        print(f'#{i} >')
    elif case[0] < case[1]:
        print(f'#{i} <')
    else:
        print(f'#{i} =')