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

def solution(participant, completion):
    participant_sort = sorted(participant)
    completion_sort = sorted(completion)

    for p,q in zip(participant_sort, completion_sort):
        if p != q:
            return p
    
    return participant_sort[-1]

print(solution(	["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))