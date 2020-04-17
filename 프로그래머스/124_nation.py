# 124 나라의 숫자

def solution(n):
    answer = ''
    num = ['1', '2', '4']
    result = []
    n = n+1
    while True:
        a, b = divmod(n, 3)
        result.append(str(b))
        n = a
        if a < 3 :
            result.append(str(a))
            break
    # for i in range(len(result)-1, -1, -1):
    #     answer += num[int(result[i])]
    for i in range(len(result)-1, -1, -1):
        answer += num[int(result[i])]


    return answer

print(solution(5))