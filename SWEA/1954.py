# 달팽이 숫자
# size = 4인 경우
# 4 33 22 11
def snail(size):
    result = []
    tmp = list(range(1, size*size+1))
    for i in range(0, size):
        result.append(tmp[size*i:size*i+size])
    row, col = 0, -1
    tmp = 1
    count = 1
    while True:

        # 가로를 채운다
        for _ in range(size):
            col += tmp
            result[row][col] = count
            count+=1
        size -= 1    

        if size == 0:
            break
        # 세로를 채운다
        for _ in range(size):
            row += tmp
            result[row][col] = count
            count += 1
        # 거꾸로 가며 채운다
        tmp = -tmp
    return result

case = int(input())

for T in range(1, case+1):
    size = int(input())
    arr = snail(size)
    print(f'#{T}')
    for i in arr:
        for j in i:
            print(j, end=' ')
        print('')
        
