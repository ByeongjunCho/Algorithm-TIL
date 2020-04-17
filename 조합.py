# 조합
# 5개에서 3개를 뽑는 조합의 가짓수
s = [0] * 3
def comb(k, start):
    if k == 3:
        print(s)
        return

    for i in range(start, len(nums)):
        s[k] = nums[i]
        # s.append(nums[i])
        comb(k+1, i+1)
        # s.pop()

nums = [1,2,3,4,5]
comb(0, 0)