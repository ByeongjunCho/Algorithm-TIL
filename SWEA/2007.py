# 패턴 마디의 길이

# case = int(input())
case = 1
string = 'GALAXYGALAXYGALAXYGALAXYGALAXY'

for c in range(case):
    # string = input()
    for n in range(2,11):
        if string[:n+1] == string[n:2*n+1]:
            print(f'#{c+1} {n}')
            break
        else:
            continue