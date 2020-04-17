# 완전탐색-모의고사
# def solution(answers):
#     answer = []
#     s1 = [1, 2, 3, 4, 5]
#     s1 = [1, 2, 3, 4, 5] * (len(answers)//len(s1) + 1)
#     s2 = [2, 1, 2, 3, 2, 4, 2, 5]
#     s2 = [2, 1, 2, 3, 2, 4, 2, 5] * (len(answers)//len(s2) + 1)
#     s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
#     s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (len(answers)//len(s3) + 1)
#     s = [s1, s2, s3]
    
#     for ss in s:
#         count = 0
#         for p, q in zip(answers, ss):
#             if p==q:
#                 count += 1
#         answer.append(count)
#     max_answer = max(answer)
#     # if answer.count(max_answer) > 1:
    
#     idx_list = []
#     for i in range(len(answer)):
#         if answer[i] == max_answer:
#             idx_list.append(i+1)
#     return idx_list

def solution(answers):
    
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer = [0, 0, 0]
    for idx, val in enumerate(answers):

        if val == s1[idx%len(s1)]:
            answer[0] += 1
        if val == s2[idx%len(s2)]:
            answer[1] += 1
        if val == s3[idx%len(s3)]:
            answer[2] += 1
            
    mymax = max(answer)
    result = []
    for i in range(len(answer)):
        if answer[i] == mymax:
            result.append(i+1)
    return result
            
        
print(solution([1,2,3]))
print(solution([1,3,2,4,2]))
# print(solution([2, 1, 2, 3, 2, 4, 2, 5]*17))