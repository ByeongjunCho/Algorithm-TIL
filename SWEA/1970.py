# 쉬운 거스름돈

def cash(num):
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    coin = []
    for mo in money:
        coin.append(num//mo)
        num -= (num//mo) * mo
    return coin

T = int(input())

for case in range(T):
    money = int(input())
    print(f'#{case+1}')
    for k in cash(money):
        print(k, end =' ')
    print('')