print(ord('a'))
print(chr(65))
print(ord('ㄱ'))
import sys
print(sys.getdefaultencoding())

arr = 'algorithm'
# print(arr[::-1])
arr = list(arr)
print(arr)
N = len(arr)
for i in range(N//2):
    # arr[i] <---> arr[N-1-i]
    arr[i], arr[N-1-i] = arr[N-1-i], arr[i]
print(arr)
print('aaa' == 'aab')
print('aaa' > 'aab')
print('aaa' < 'aab')

# atoi
arr = '123456'

val = 0
for c in arr:
    val = val * 10 + (ord(c) - ord('0'))

print(val)

val_str = ''
while val:
    print(val % 10)
    val = val // 10