# 수열 기초
"""
1, 2, 3으로 순열 만들기
첫째 자리      1              2             3
둘째 자리   12    13       21    23       31   32
셋째 자리  123    132     213    231    312    321
완성
"""


a = [1,2,3]  # 사용할 숫자
used = [0] * len(a)  # 사용된 숫자 기록
p = [0] * len(a)  # 선택된 숫자 기록

def perm(k):
    if k == len(a):
        print(p)

    for i in range(len(a)):
        if used[i]:
            continue
        used[i] = 1
        p[k] = a[i]
        perm(k+1)
        used[i] = 0

perm(0)
