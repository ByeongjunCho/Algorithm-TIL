# 새로운 불면증 치료법

def insomnia(num):
    count_set = set()
    count = 1
    while True:
        count_set.update(set(list(str(num*count))))
        if len(count_set) == 10:
            break
        count += 1
    print(count_set)
    return count


case = int(input())

for T in range(1, case+1):
    number = int(input())
    print(f'#{T} {insomnia(number)*number}')
