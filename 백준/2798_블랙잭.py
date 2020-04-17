N, M = map(int, input().split())
cards = list(map(int, input().split()))
cards.sort(reverse=True)
result = 0

def black(k, start, vals):
    global M, N, result
    if vals > M:
        return
    if k == 3:
        result = max(result, vals)
        return

    for i in range(start, N):
        black(k+1, i+1, vals+cards[i])
black(0, 0, 0)
print(result)
    
