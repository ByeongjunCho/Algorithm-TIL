lotto = [0] * 6
def comb(k, start):
    if k == 6:
        print(' '.join(lotto))
        # print(lotto)
        return

    for i in range(start, int(S[0])+1):
        lotto[k] = S[i]
        comb(k+1, i+1)
        

while True:
    S = input().split()
    if S[0] == '0':
        break
    comb(0, 1)
    print()
