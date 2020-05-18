'''
boj 17281번-야구
순열사용
'''

def playGame(start, players, inning):
    score = 0
    outcnt = 0
    ground = [0, 0, 0]
    curnum = start  # 플레이를 할 사람의 번호
    while outcnt < 3:
        # 현재 플레이어의 행동
        curplay = inning[players[curnum]]
        if not curplay:
            outcnt += 1
        else:
            for i in range(2, -1, -1):
                if ground[i] and i+curplay > 2:
                    ground[i] = 0
                    score += 1
                elif ground[i]:
                    ground[i] = 0
                    ground[i+curplay] = 1
            if curplay <=3:
                ground[curplay-1] = 1
            elif curplay == 4:
                score += 1

        # 다음 선수 출전
        curnum += 1
        if curnum > 8:
            curnum = 0

    # 현재이닝에서 얻은 점수, 다음이닝에 출전할 선수 번호
    return score, curnum



players = list(range(1,9))

def perm(k):
    if k == len(players):
        p = players[0:3] + [0] + players[3:]
        tmp = 0

        startnum = 0
        for inning in M:
            s, startnum = playGame(startnum, p, inning)
            tmp += s

        global result
        result = max(result, tmp)

        return

    for i in range(k, len(players)):
        players[k], players[i] = players[i], players[k]
        perm(k+1)
        players[i], players[k] = players[k], players[i]


N = int(input())
M = [list(map(int, input().split())) for _ in range(N)]

result = 0

perm(0)
print(result)