'''
boj 16637번-괄호 추가하기
backtracing을 이용한 풀이
'''

def calc(operand1, operand2, operator):
    if operator == '+':
        return operand1+operand2
    elif operator == '-':
        return operand1 - operand2
    else:
        return operand1 * operand2

def back(k, val):
    if k >= len(operands):
        global result
        result = max(result, val)
        return
    # 괄호없이 계산한 경우
    back(k+1, calc(val, operands[k], operators[k-1]))
    # 괄호가 있는 경우
    if k+1 < len(operands):
        back(k+2, calc(val, calc(operands[k], operands[k+1], operators[k]), operators[k-1]))


N = int(input())
tmp = input()
operands = []
operators = []

# 연산자와 숫자를 분리
for i in range(N):
    if tmp[i] in ['+', '-', '*']:
        operators.append(tmp[i])
    else:
        operands.append(int(tmp[i]))

result = -0xffffff
back(1, operands[0])
print(result)