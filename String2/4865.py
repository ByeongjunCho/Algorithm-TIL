# 4865. [파이썬 S/W 문제해결 기본] 3일차 - 글자수


def max_alpha(str1, str2):
    pattern = set(str1)

    max_count = 0
    for char in pattern:
        count = 0
        for j in range(len(str2)):
            if char == str2[j]:
                count += 1
        if count > max_count:
            max_count = count
    return max_count

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()
    print('#{} {}'.format(test_case, max_alpha(str1, str2)))