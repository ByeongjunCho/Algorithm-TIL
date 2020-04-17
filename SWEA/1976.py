# 시각 덧셈

def time_sum(t1, m1, t2, m2):
    time = t1 + t2
    minute = m1 + m2
    if  minute >= 60:
        minute -= 60
        time += 1

    if time > 12:
        time -= 12
    return time, minute

case = int(input())

for t in range(case):
    t1, m1, t2, m2 = map(int, input().split())
    time, minute = time_sum(t1, m1, t2, m2)
    print(f'#{t+1} {time} {minute}')
    