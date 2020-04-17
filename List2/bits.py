arr = 'ABC'
bits = [0] * 3

for i in range(2):
    bits[0] = i
    for i in range(2):
        bits[1] = i
        for i in range(2):
            bits[2] = i
            print(bits, end='> ')
            for i in range(len(bits)):
                if bits[i]: print(arr[i], end=' ')
            print()

def subset(k, n):
    if k==n:
        print(bits, end='> ')
        for i in range(len(bits)):
            if bits[i]: print(arr[i], end=' ')
        print()
        return
    for i in range(2):
        bits[k] = i
        # 재귀 호출
        subset(k+1, n)

a = 0b1010
b = 0b1100
c = a&b
print(bin(a))
print(bin(a << 1))
print(bin(a >> 1))

n = 10
if n & 1:
    print('홀수')
else:
    print('짝수')