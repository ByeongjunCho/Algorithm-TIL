# 수도 요금 경쟁
def cost(P, Q, R, S, W):
    A_cost = P * W
    if W > R:
        B_cost = Q + S * (W-R)
    else:
        B_cost = Q
    return A_cost if A_cost < B_cost else B_cost

test_case = int(input())
for T in range(1, 1+test_case):
    P, Q, R, S, W = list(map(int, input().split()))
    print(f'#{T} {cost(P, Q, R, S, W)}')