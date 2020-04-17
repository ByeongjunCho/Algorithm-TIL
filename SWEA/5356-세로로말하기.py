
T = int(input())

for tc in range(1, T+1):
    print('#{} '.format(tc), end='')
    string = [input() for _ in range(5)]
    my_len = 0
    for s in string:
        my_len = max(my_len, len(s))


    for i in range(my_len):
        for s in string:
            try:
                print(s[i], end='')
            except:
                continue
    print()
