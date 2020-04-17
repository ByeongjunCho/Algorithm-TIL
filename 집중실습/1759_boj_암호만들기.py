# def password(k, L, C, s):
#     if k == L:
#         print(s)
#         return
#     for i in range(k, L+k-1):
#         if alpabet[i] in s:
#             continue
#         password(k+1, L, C, s+alpabet[i])
#
# L, C = map(int, input().split())
# alpabet = input().split()
#
# alpabet.sort()
# password(0, L, C, '')

## 부분집합을 이용한 풀이

# pwd = []
# alpha = ('a', 'e', 'i', 'o', 'u')
# def backtrack(k, mo, ja):
#     if len(pwd) == L:
#         print(pwd)
#         return
#     if k == C: return
#     a = b = 0
#     pwd.append(arr[k])
#     if arr[k] in alpha: a=1
#     else: b=1
#     backtrack(k+1, mo+a, ja+b)    # k번째 요소를 포함하는 경우
#     pwd.pop()
#     backtrack(k+1, mo, ja)    # k번째 요소를 포함하지 않는 경우
#
# L, C = map(int, input().split())
# arr = list(input().split())
# arr.sort()
#
# backtrack(0, 0, 0)


moeum = ['a', 'e', 'i', 'o', 'u']
result = []
def comb(k, start, mo, ja):
    if k == L:
        if mo >= 1 and ja >= 2:
            result.append(''.join(order))
        return

    for i in range(start, C):
        order[k] = arr[i]
        if arr[i] in moeum:
            comb(k+1, i + 1, mo+1, ja)
        else:
            comb(k+1, i+1, mo, ja+1)
        order[k] = 0


L, C = map(int, input().split())
order = [0] * L
arr = list(input().split())
arr.sort()
comb(0, 0, 0, 0)
for c in result:
    print(c)