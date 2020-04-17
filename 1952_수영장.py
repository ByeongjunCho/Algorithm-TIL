# 1952. [모의 SW 역량테스트] 수영장
## 1. DP 사용

def use_dp():
    T = int(input())

    for tc in range(1, T+1):
        D, M, M3, Y = map(int, input().split())
        plan = list(map(int, input().split()))
        cost = [0 for _ in range(13)]
        cost[1] = min(plan[0] * D, M)

        for i in range(2, len(cost)):
            cost[i] = cost[i - 1] + min(plan[i-1] * D, M)
            if i > 2:
                cost[i] = min(cost[i], cost[i-3] + M3)

        print("#{} {}".format(tc, min(Y, cost[12])))

def use_back():
    def back(k, val):
        if k > 11:
            mymin[0] = min(mymin[0], val)
            return
        elif mymin[0] < val:
            return
        # 일일 이용권 / 한달 이용권
        back(k+1, val + min(plan[k] * D, M))
        # 3달 이용권
        back(k+3, val + M3)

    T = int(input())

    for tc in range(1, T + 1):

        D, M, M3, Y = map(int, input().split())
        plan = list(map(int, input().split()))
        mymin = [Y]
        back(0, 0)

        print("#{} {}".format(tc, mymin[0]))

use_back()