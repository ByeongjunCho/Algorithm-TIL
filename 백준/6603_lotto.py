arr = [1, 2, 3]
def permutation(n):
    if n == 2:
        print(arr)
        return 
    
    for i in range(n, 3):
        arr[i], arr[n] = arr[n], arr[i]
        permutation(n+1)
        arr[n], arr[i] = arr[i], arr[n]

permutation(0)

arr = [1, 2, 3, 4, 5]
def permutation(n, r):   # n: 배열의 기준점(0부터 시작) r: 원하는 길이 
    if n == r:
        print(arr)
        return 
    
    for i in range(n, len(arr)):
        arr[i], arr[n] = arr[n], arr[i]
        permutation(n+1, r)
        arr[n], arr[i] = arr[i], arr[n]

permutation(0, 3)

def combination(n, r):
    if n == r or r == 0: 
        return 1
    else:
        return combination(n-1, r-1) + combination(n-1, r)

print(combination(3, 2)
