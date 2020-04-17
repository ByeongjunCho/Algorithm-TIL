# 조교의 성적 매기기


def degree(score_list_len, score_list, student_num):
    score_target = score_list[student_num - 1]
    degree_list = ['A+', 'A0', 'A-',
        'B+','B0','B-','C+',
        'C0','C-','D0']
    score_sort = sorted(score_list, reverse = True)
    score_target_index = score_sort.index(score_target)
    degree = round((score_target_index / (score_list_len // 10)) + 0.500001)
    return degree_list[degree - 1]


tset_case = int(input())

for case in range(tset_case):
    student_numbers, student_num = list(map(int, input().split()))
    scores = []
    for num in range(student_numbers):
        mid, final, report = list(map(int, input().split()))
        # scores.append(round(0.35*mid + 0.45*final + 0.2*report, 3))
        scores.append(0.35*mid + 0.45*final + 0.2*report)
    print(f'#{case+1} {degree(student_numbers, scores, student_num)}')