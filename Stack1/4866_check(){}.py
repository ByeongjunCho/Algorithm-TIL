# 4866. [파이썬 S/W 문제해결 기본] 4일차 - 괄호검사


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    string = input()
    stack = []
    try:
        for s in string:
            if s == '(' or s == '{':
                stack.append(s)
                continue
            if s == ')':
                if stack.pop() != '(':
                    print('#{} 0'.format(test_case))
                    break
            elif s == '}':
                if stack.pop() != '{':
                    print('#{} 0'.format(test_case))
                    break
        else:
            if len(stack):
                print('#{} 0'.format(test_case))
            else:
                print('#{} 1'.format(test_case))


    except:
        print('#{} 0'.format(test_case))
        continue


