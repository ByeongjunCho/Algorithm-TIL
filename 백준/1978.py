
N = int(input())
numbers = list(map(int, input().split()))
prime_count = 0
for num in numbers:
    if num == 1 or num == 0:
        continue
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            break
    else:
        prime_count += 1

print(prime_count)