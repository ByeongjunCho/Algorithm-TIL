T = int(input())
for tc in range(1, T+1):
    N, htob = input().split()
    # htob = bin(int(htob, 16))[2:]
    # htob = '0' * ((int(N)*4) - len(htob)) + htob
    # print('#{} {}'.format(tc, htob))