# 1206. [S/W 문제해결 기본] 1일차 - View

# import sys
# sys.stdin = open('input.txt', 'r')
def my_max(*args):
    max_result = args[0]
    for i in range(len(args)):
        if max_result < args[i]:
            max_result = args[i]
    return max_result

for T in range(1, 11):
    test_len = int(input())
    # a, b = map(int, input().split())
    testcase = list(map(int, input().split()))
    result = 0
    for i in range(2, test_len-2):
        tmp = testcase[i] - my_max(testcase[i-2], testcase[i-1], testcase[i+1], testcase[i+2])
        if tmp > 0:
            result += tmp
    # print(f'#{T} {result}')
    print('#%d %d' % (T, result))
