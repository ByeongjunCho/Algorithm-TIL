# 4012. [모의 SW 역량테스트] 요리사
import sys
sys.stdin = open('sample_input.txt', 'r')

def cook_min(arr, N):
    min_cook = 20000 * 16
    for i in range(1<<N):
        cook = list(range(N))
        cook_tmp = cook[:]
        tmp1 = 0  
        tmp2 = 0
        tmp = []
        for j in range(len(arr)):
            if i&(1<<j):
                tmp.append(cook_tmp[N-1-j])
        # tmp = [cook_tmp[N-1-x] for x in range(len(arr)) if i&(1<<x)]
                
        if len(tmp) != N/2:
            continue
        
        else:

            for i in range(len(tmp)):
                cook.pop(tmp[i])

            for i in range(len(cook)):
                for j in range(len(cook)):
                    tmp1 += arr[tmp[i]][tmp[j]]
                    tmp2 += arr[cook[i]][cook[j]]

            if min_cook > abs(tmp1-tmp2):
                min_cook = abs(tmp1-tmp2)
    return min_cook

for T in range(1, int(input())+1):
    N = int(input())
    test_arr = []
    for _ in range(N):
        test_arr.append(list(map(int, input().split())))
    print('#{} {}'.format(T, cook_min(test_arr, N)))


# 요리사
# 식재료를 2 그룹으로 나누어야 된다.
# N개의 식재료 --> N/2, N/2
# N = 16 최대 --> 2^16 = 65536

arr = 'ABCD'
N = 4
for set in range(1 << N):
    A, B = [], []
    for i in range(N):
        if set & (1<<i):
            A.append(arr[i])
        else:
            B.append(arr[i])
    if len(A) == len(B):
        print(A, B)