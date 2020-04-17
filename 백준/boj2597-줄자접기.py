N = int(input())
red = map(int, input())
blue = map(int,input())
yellow = map(int,input())

a = [0] * (N+1)
result = N
# red
r = (red[0] + red[1])/2
result = min(N - r, r)
# 조정
if N-r > r:  # 뒤에 것을 앞으로
    if blue[0] < r:
        blue[0] = r + (r-blue[0])
    if blue[1] < r:
        blue[1] = r + (r-blue[1])
    if yellow[0] < r:
        yellow[0] = r + (r-yellow[0])
    if yellow[1] < r:
        yellow[1] = r + (r - yellow[1])
elif N-r < r:
    if blue[0] > r:
        blue[0] = r - (blue[0]-r)
    if blue[1] > r:
        blue[1] = r - (blue[1]-r)
    if yellow[0] > r:
        yellow[0] = r - (yellow[0]-r)
    if yellow[1] > r:
        yellow[1] = r - (yellow[1]-r)
N = min(N-r, r)
blue