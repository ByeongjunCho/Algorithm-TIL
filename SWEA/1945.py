def small_prime(num):
    numbers = [2, 3, 5, 7, 11]
    result = []
    for n in numbers:
        count = 0
        while True:
            if num % n:
                break
            else:
                count += 1
                num /= n
        result.append(count)
    return result

case = int(input())

for T in range(1, case+1):
    number = int(input())
    print(f'#{T}', end=' ')
    for i in small_prime(number):
        print(i, end=' ')
    print('')