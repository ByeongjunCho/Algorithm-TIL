arr = [0, 4, 1, 3, 1, 2, 4, 1]
# 양의 정수, 최대값을 알아야 한다.
# 최대값 = 4
cnt = [0] * 5 # 배열의 인덱스 n-1 = 4
# 빈도수 계산
for val in arr:
    cnt[val] += 1
print(cnt)

result = []
for i in range(len(cnt)):
    for j in range(cnt[i]):
        # i가 cnt[i] 만큼 반복되는 것
        result.append(i)
print(result)

# 누적 빈도수 계산
for i in range(1, len(cnt)):
    cnt[i] += cnt[i-1]

result = [0] * len(arr)
for i in range(len(arr), -1, -1):
    