# 지그재그 숫자

test_case = int(input())

def zigzag(n):
    result = 0
    for i in range(1, n+1):
        result += i if i % 2 else -i
    return result


for case in range(1, test_case + 1):
    number = int(input())
    print(f'#{case} {zigzag(number)}')