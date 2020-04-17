# 369게임

num = int(input())

def change_369(n):
    tmp = ''
    if '3' in str(n) or '6' in str(n) or '9' in str(n):
        for s in list(str(n)):
            if s in '369':
                tmp += '-'
        else: 
            return tmp
    else:
        return str(n)


# print(change_369(14))

for n in range(1, num + 1):
    print(change_369(n), end=' ')