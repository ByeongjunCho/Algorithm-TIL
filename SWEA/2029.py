test_case = int(input())

for case in range(test_case):
    a, b = map(int, input().split(' '))
    print(f'#{case + 1} {a // b} {a % b}')