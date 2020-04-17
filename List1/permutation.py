# 순열 구하기
arr = 'ABC'
n = len(arr)
for i in range(n):  # 첫번째 위치 데이터
    for j in range(n): # 두번째 위치 데이터
        if j==i: continue
        for k in range(n): # 세번째 위치 데이터
            if k==i or k==j: continue
            print(arr[i], arr[j], arr[k])
