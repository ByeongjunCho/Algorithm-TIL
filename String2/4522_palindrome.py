# 4522. 세상의 모든 팰린드롬

def Pal(string):
    lenth = len(string)
    for i in range(lenth >> 1):
        if (string[i] != string[lenth-1-i]) and (string[i] != '?' and string[lenth-1-i] != '?'):
            return 'Not exist'
    return 'Exist'

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    test_string = input()
    print('#{} {}'.format(test_case, Pal(test_string)))
