s = set()
def all_vals(k, score):
    if k == N:
        s.add(score)
        return

    all_vals(k+1, score+vals[k])
    all_vals(k+1, score)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    vals = list(map(int, input().split()))
    all_vals(0, 0)
    print('#{} {}'.format(tc, len(s)))
    s = set()

