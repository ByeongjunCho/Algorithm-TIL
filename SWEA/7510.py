# 상원이의 연속 합

def sangwon(num):
    if num == 1:
        return 1
    sum_all = 0
    count = 1
    for i in range(1, round(num/2 + 0.1) + 1):
        sum_all = 0
        for j in range(i, round(num/2 + 0.1) + 1):
            sum_all += j
            if sum_all == num:
                count+=1
                break
            elif sum_all > num:
                break
    return count

print(sangwon(5))