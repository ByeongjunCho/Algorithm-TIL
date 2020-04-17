small = [0] * 9
for i in range(9):
    small[i] = int(input())


result = []
tmp = [0]*7
def comb(k, start, ans):
    if k == 7:
        if ans == 100:
            for i in range(7):
                tmp[i] = result[i]
            return True
        return

    for i in range(start, 9):
        result.append(small[i])
        a = comb(k+1, i+1, ans+small[i])
        result.pop()
        if a:
            break


comb(0, 0, 0)
tmp.sort()
for c in tmp:
    print(c)