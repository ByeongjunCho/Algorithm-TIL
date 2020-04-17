t_case = int(input())

for i in range(1, 1+t_case):
    case = input()
    y, m, d = case[0:4], case[4:6], case[6:]
    int_m, int_d = int(m), int(d)
    if int_m in [1, 3, 5, 7, 8, 10, 11]:
        if int_d in range(1,32):
            print(f'#{i} {y}/{m}/{d}')
        else:
            print(f'#{i} -1')
    elif int_m in [4, 6, 9, 11]:
        if int_d in range(1, 31):
            print(f'#{i} {y}/{m}/{d}')
        else:
            print(f'#{i} -1')
    elif int_m in [2]:
        if int_d in range(1,30):
            print(f'#{i} {y}/{m}/{d}')
        else:
            print(f'#{i} -1')
    else:
        print(f'#{i} -1')
    
    # print(f'#{i} {max(case)}')