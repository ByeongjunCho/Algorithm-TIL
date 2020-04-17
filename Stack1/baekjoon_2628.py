# 2628 종이자르기

width, height = map(int, input().split()) # 가로/세로
set1 = {0, width} # 가로값 보관
set2 = {0, height} # 세로값 보관


for _ in range(int(input())):
    status, idx = map(int, input().split())
    if status:
        set1.update({idx})
    else:
        set2.update({idx})
col = sorted(list(set1))
row = sorted(list(set2))

my_max = 0
for i in range(len(col)-1):
    for j in range(len(row)-1):
        if (col[i+1] - col[i]) * (row[j+1] - row[j]) > my_max:
            my_max = (col[i+1] - col[i]) * (row[j+1] - row[j])
print(my_max)