# 스킬트리

def check_(le1):
    for i in range(len(le1) -1):
        if le1[i+1] - le1[i] < 0 and le1[i] >= 0 and le1[i+1] >= 0: # 오름차순이 아니면서 -1이 없는 경우
            return 0
        elif le1[i] < 0 or le1[i+1] < 0:  # -1이 있다면 뒤 모든것이 -1인지 확인한다.
            for j in range(i+1, len(le1)):
                if le1[j] != -1:
                    return 0
            return 1
    else:
        return 1



def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        skill_tmp = []
        for i in skill:
            skill_tmp.append(tree.find(i))
        print(skill_tmp)
        answer += check_(skill_tmp)


    return answer

print(solution("CBD", ['BACDE', 'CBADF', 'AECB', 'BDA', 'CED']	))

