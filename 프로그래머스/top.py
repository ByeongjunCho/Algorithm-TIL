# 코딩테스트 연습 스택/큐 탑

def solution(heights):
    answer = [0] * len(heights)
    count = len(heights) - 1
    while True:
        val = heights.pop()
        for i in range(len(heights)-1, -1, -1):
            if val < heights[i]:
                answer[count] = i+1
                break
        count -= 1
        if len(heights) == 1:
            break
    return answer

def solution(heights):
    answer = [0] * len(heights)
    for i in range(len(heights)-1, -1, -1):
        for j in range(i, -1, -1):
            if heights[j] > heights[i]:
                answer[i] = j+1
                break

    return answer
print(solution([1,5,3,6,7,6,5]))