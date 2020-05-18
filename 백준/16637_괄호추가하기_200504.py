'''
boj 16637번-괄호 추가하기
backtracing을 이용한 풀이
'''

def calc(oper1, oper2, sig):
    if sig == '-':
        return oper1 - oper2
    elif sig == '*':
        return oper1*oper2
    else:
        return oper1+oper2

def back(k, val):
    global N, result
    if k >= N//2:
        result = max(result, val)
        return
    
    # 괄호 없이 계산하는 경우
    # len(operand) = N//2 + 1(언제나 operator보다 1많음)
    # len(operator) = N//2
    back(k+1, calc(val, operand[k+1], operator[k]))

    # 괄호를 추가하여 계산하는 경우
    if k+2 <= N//2:
        back(k+2, calc(val, calc(operand[k+1], operand[k+2], operator[k+1]), operator[k]))


N = int(input())
M = list(input())

operator = []
operand = []

for v in M:
    if v in ['+', '-', '*']:
        operator.append(v)
    else:
        operand.append(int(v))

result = -0xffffff
back(0, operand[0])

print(result)