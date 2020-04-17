# 스위치 켜고 끄기


switch_num = int(input())
switch_status = list(map(int, input().split()))
student_num = int(input())

student = []
for _ in range(student_num):
    student.append(list(map(int, input().split())))

for i in range(len(student)):
    person_status = student[i][0]
    person_num = student[i][1]
    # 남학생인 경우
    tmp = 1 # 배수를 위한 임시값
    if person_status == 1:
        while True:
            if person_num * tmp - 1 > switch_num-1:
                break
            switch_status[person_num * tmp - 1] = not switch_status[person_num * tmp - 1]
            tmp += 1
    # 여학생의 경우
    tmp = 1 # 좌우 확인을 위한 임시값
    if person_status == 2:
        switch_status[person_num - 1] = not switch_status[person_num - 1]
        while True:
            if (person_num -1 - tmp) < 0 or (person_num -1 + tmp) > switch_num-1:
                break
            if switch_status[person_num-1 - tmp] == switch_status[person_num-1 + tmp]:
                switch_status[person_num-1 - tmp] = not switch_status[person_num - 1 - tmp]
                switch_status[person_num-1 + tmp] = not switch_status[person_num-1 + tmp]
            else:
                break
            tmp += 1

switch_status = list(map(int, switch_status))

for i in range(switch_num):
    # 마지막이 아니고 20번째가 아니라면,
    if i != switch_num-1 and (i+1) % 20 != 0:
        print(str(switch_status[i]), end=' ')
    elif (i+1) % 20==0:
        print()
    else:
        print(str(switch_status[i]), end='')
