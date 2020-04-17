## C-style
# S = [0] * 3
# top = -1
#
# def push(item):
#     global top
#     # full-상태에 주의 if top == 마지막 인덱스:
#     top += 1
#     S[top] = item
#
# def pop():
#     # empty 상태 체크
#     if top == -1: return
#     ret = S[top]
#     top -= 1
#     return ret

S = []
S.append(1) # push
S.append(2) # push
S.append(3) # push

print(S.pop())
print(S.pop())
print(S.pop())
