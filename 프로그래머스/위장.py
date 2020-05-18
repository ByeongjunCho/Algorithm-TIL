def solution(clothes):
    dic = dict()
    for value, key in clothes:
        if dic.get(key):
            dic[key] += 1
        else:
            dic[key] = 2
    
    answer = 1
    for value in dic.values():
        answer *= value
    return answer - 1