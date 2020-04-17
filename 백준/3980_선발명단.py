C = int(input())
arr = [list(map(int, input().split())) for _ in range(11)]

result = 0
def perm(k, used, vals):
    if k == 11:
        global result
        result = max(result, vals)

    for i in range(11):
        if used & (1 << i):
            continue
        if not arr[k][i]:
            continue
        perm(k+1, used | (1 << i), vals+arr[k][i])
perm(0, 0, 0)
print(result)
