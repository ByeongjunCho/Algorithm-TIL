# 1989. 초심자의 회문 검사


def Pal(string):
    N = len(string)
    for i in range(N >> 1):
        string[i], string[N - 1 - i] = string[N - 1 - i], string[i]
    return string


test_case = int(input())

# for case in range(1, test_case + 1):
#     string = input()
#     if string == string[::-1]:
#         print(f'#{case} 1')
#     else:
#         print(f'#{case} 0')

for case in range(1, test_case + 1):
    string = list(input())

    if string == Pal(string):
        print('#{} 1'.format(case))
    else:
        print('#{} 0'.format(case))