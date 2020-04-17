# 초심자의 회문 검사

test_case = int(input())

for case in range(1, test_case+1):
    string = input()
    if string == string[::-1]:
        print(f'#{case} 1')
    else:
        print(f'#{case} 0')