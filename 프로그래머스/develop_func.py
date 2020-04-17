

def check(days):
    result = []  # 결과를 담을 변수
    start = 0 # 시작값
    idx = 1 # 중간값
    count = 1 # 몇 개의 기능이 있는지 count

    while True:
        if idx == len(days):
            result.append(count)
            break
        if days[start] < days[idx]:
            result.append(count)
            start = idx
            idx += 1
            count = 1
        else:
            idx += 1
            count += 1
    return result
def solution(progresses, speeds):
    tmp_days = []

    # 각 기능마다 필요한 시간을 구한다
    for i in range(len(progresses)):
        day = (100 - progresses[i]) / speeds[i]
        if day > (100 - progresses[i]) // speeds[i]:
            day = round(day + 0.5)
        tmp_days.append(int(day))
    answer = check(tmp_days)

    return answer

def solution(progresses, speeds):
    answer = []

    return answer



# print(check([17,3,15,14,18]))
print(solution([93,30,55], [1,30,5]))