# def solution(priorities, location):
#     tmp = priorities[:]
#     idx = 0 # idx_list의 포인터
#     length = len(priorities)
#     idx_list = list(range(length))
#     count = 1
#     tmp_idx = -1
#     while True:
#         for k in range(idx+1, length+idx):
#             if tmp[idx_list[idx]] < tmp[idx_list[k]]:
#                 idx_list.append(idx_list[idx])
#                 idx += 1
#                 break
#         else:
#             try:
#                 tmp_idx = idx_list.pop(idx)
#                 count += 1
#                 length -= 1
#             except:
#                 return count-1
#
#         if tmp_idx == location:
#             return count-1



def solution(priorities, location):
    max_p = max(priorities)
    count = 0

    while True:
        m = priorities.pop(0)
        if max_p == m:
            count += 1
            if location == 0:
                break
            else:
                location -= 1
            max_p = max(priorities)
        else:
            priorities.append(m)
            if location == 0:
                location = len(priorities)-1
            else:
                location -= 1
    return count


print(solution([2,1,3,2], 1))