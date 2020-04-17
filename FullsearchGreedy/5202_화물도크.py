T = int(input())
for tc in range(1, T+1):
    N = int(input())
    case = [0] * N
    for i in range(N):
        s, e = map(int, input().split())
        case[i] = (e, s)
    case.sort()  # 종료시간을 기준으로 정렬

    result = 0 # 결과값 저장
    timesheet = [0] * 24 # 시간표
    for i in range(N):
        end, start = case[i]
        # start부터 end까지 timesheet가 비어있는지 확인
        for j in range(start, end):
            if timesheet[j]:
                break
        else:  # 비어있다면 1로 채우고 결과값에 1을 더함
            for j in range(start, end):
                timesheet[j] = 1
            result += 1
    print('#{} {}'.format(tc, result))