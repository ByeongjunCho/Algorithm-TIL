# 4874. [파이썬 S/W 문제해결 기본] 5일차 - Forth


def calc(string):
    S = []
    try:
        for c in string:
            if c == '+':
                u = int(S.pop())
                v = int(S.pop())
                S.append(v+u)
            elif c == '-':
                u = int(S.pop())
                v = int(S.pop())
                S.append(v - u)
            elif c == '*':
                u = int(S.pop())
                v = int(S.pop())
                S.append(v * u)
            elif c == '/':
                u = int(S.pop())
                v = int(S.pop())
                S.append(int(v / u))
            elif c == '.':
                if len(S) != 1:
                    return 'error'
                else:
                    return S[-1]
            else:
                S.append(c)
    except:
        return 'error'
    return 'error'

T = int(input())
for tc in range(1, T+1):
    case = input().split()
    print('#{} {}'.format(tc, calc(case)))