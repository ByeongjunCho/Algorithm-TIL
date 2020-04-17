# 파스칼의 삼각형 출력
T = int(input())
def pascal(n):
    tmp = [1]
    if n == 1:
        print(tmp[0])
        return tmp

    else:
        p = pascal(n-1)
        for i in range(n-2):
            tmp.append(p[i] + p[i+1])
        tmp.append(1)
        for k in tmp:
            print(k, end=' ')
        print()
        return tmp

for i in range(T):
    number = int(input())
    print(f'#{i+1}')
    pascal(number)