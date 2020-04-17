# 간단한 압축 풀기



case = int(input())

for T in range(1, case+1):
    case_n = int(input())
    result = ''
    for _ in range(case_n):
        datas = input().split()
        result+= datas[0] * int(datas[1])
    print(f'#{T}')
    for ix, s in enumerate(result):
        print(s, end='')
        if ix > 0 and (ix+1)%10 == 0:
            print('')
    print('')