# 4012. [모의 SW 역량테스트] 요리사


def comb(start):
    if len(s) == num:
        tmp = [] # 상대 요리
        for k in range(N):
            if k not in s:
                tmp.append(k)

        cook1, cook2 = 0, 0  # 요리 합 저장
        for i in range(num):
            for j in range(num):
                cook1 += arr[s[i]][s[j]]
                cook2 += arr[tmp[i]][tmp[j]]
        global result
        result = min(result, abs(cook1-cook2))

    for i in range(start, N):
        s.append(i)
        comb(i+1)
        s.pop()


for tc in range(1, 1 + int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    num = N//2
    s = []
    result = 0xffffff
    comb(0)
    print('#{} {}'.format(tc, result))