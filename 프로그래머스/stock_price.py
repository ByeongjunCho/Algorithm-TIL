def solution(prices):
    answer = []
    for i in range(len(prices)):
        tmp = -1
        for j in range(i, len(prices)):
            tmp += 1
            if prices[i] > prices[j]:
                break
        answer.append(tmp)
    return answer

a = solution([4,3,6,4])
print(a)