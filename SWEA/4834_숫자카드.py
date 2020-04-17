# 숫자 카드

N = int(input())
card_number = list(map(int, list(input())))
# 카드 숫자가 나온 횟수만큼 담는다.
result = [0] * 10
for i in card_number:
    result[i] += 1
# 카드를 뒤집는다.
result = list(reversed(result))
max_value = max(result)
max_index = 9 - result.index(max_value)

# print(f'#{T} {max_index} {max_value}')
print(f'# {max_index} {max_value}')