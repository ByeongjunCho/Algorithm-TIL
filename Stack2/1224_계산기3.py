# 1224. [S/W 문제해결 기본] 6일차 - 계산기3

import sys
sys.stdin = open('1224_input.txt', 'r')

calc = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}  # '(': 0
for tc in range(1, 11):
    tc_len = int(input())
    string = input()
    # 후위표기법 변환
    S = []   # 스택
    result = [] # 결과값
    status = 0
    for c in string:
        if c == '(':  # and not status:
            S.append(c)
            # status = 1
        elif c == ')': #and status:
            u = S.pop()
            while u != '(':
                result.append(u)
                u = S.pop()
            # status = 0
        elif c in calc.keys():
            if not S:
                S.append(c)
            else:
                if calc[S[-1]] >= calc[c]:   # 스택에 입력값보다 우선순위가 큰 연산자가 들어오면,
                    while True:
                        u = S.pop()
                        result.append(u)
                        if not S:
                            S.append(c)
                            break
                        elif calc[S[-1]] < calc[c]:
                            S.append(c)
                            break
                else:
                    S.append(c)
        else:
            result.append(c)
    if S:
        for val in S:
            result.append(val)

    # 후위표기법 계산

    for c in result:
        if c == '+':
            u = S.pop()
            v = S.pop()
            S.append(v + u)
        elif c == '-':
            u = S.pop()
            v = S.pop()
            S.append(v - u)
        elif c == '*':
            u = S.pop()
            v = S.pop()
            S.append(v * u)
        elif c == '/':
            u = S.pop()
            v = S.pop()
            S.append(v / u)
        else:
            S.append(int(c))
    print('#{} {}'.format(tc, S[-1]))











