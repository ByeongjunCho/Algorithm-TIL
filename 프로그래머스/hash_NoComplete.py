# def solution(participant, completion):
#     completion_dict = {}
#     for key in completion:
#         if completion_dict.get(key):
#             completion_dict[key] += 1
#         else:
#             completion_dict[key] = 1

#     for val in participant:
#         if completion_dict.get(val):
#             completion_dict[val] -= 1
#         elif completion_dict.get(val) == 0 or completion_dict.get(val) == None:
#             # completion_dict.pop(val)
#             return val



# zip를 이용한 방법
def solution(participant, completion):
    participant_sort = sorted(participant)
    completion_sort = sorted(completion)

    for p,q in zip(participant_sort, completion_sort):
        if p != q:
            return p
    
    return participant_sort[-1]

print(solution(	["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))

import collections
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)  # Counter 객체는 뺄셈이 가능
    # answer = Counter({key : value})  value가 0이면 hash에서 사라짐
    print(answer)
solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"])