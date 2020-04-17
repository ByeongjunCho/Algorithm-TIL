
def backtrack(k, vals):
    global result
    if vals > result:
        return
    if k > 11:
        result = min(result, vals)
        return

    # 그 달에 계획이 없다면 다음 달로 이동
    if not swim[k]:
        backtrack(k+1, vals)
    else:
        # 1일 이용권을 사용하는 경우
        backtrack(k+1, vals+(money[0] * swim[k]))
        # 1달 이용권을 사용하는 경우
        backtrack(k+1, vals + money[1])
        # 3달 이용권을 사용하는 경우
        backtrack(k+3, vals + money[2])


T = int(input())
for tc in range(1, T+1):
    money = list(map(int, input().split()))
    swim = list(map(int, input().split()))
    result = money[-1]
    backtrack(0, 0)
    print('#{} {}'.format(tc, result))