# Backtraking
#                     8
#         7           4          2
#     6   3   1    3  0  x    1  x  x

coin = [6, 4, 1]
choose = [0] * 100
MIN = 0xffffff
def coinChange(k, n):   # k: 선택한 동전의 수, n: 거스름돈 금액
    global MIN
    if k >= MIN: return
    if n == 0:
        MIN = min(k, MIN)

        for i in range(k):
            print(choose[i], end=' ')
        print()
        return
    for c in coin:
        if c > n: continue
        choose[k] = c
        coinChange(k+1, n-c)
    pass


coinChange(0, 8)