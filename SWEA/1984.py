# 중간값 구하기


test_case = int(input())

for case in range(1, test_case + 1):
    test_list = sorted(list(map(int, input().split())))
    print(f'#{case} {round(sum(test_list[1:9]) / 8)}')  

test_case = int(input())
for i in range(1, test_case + 1):
    sum = 0
    test_list = sorted(map(int, input().split(' ')))

    for n in test_list[1:9]:
        sum += n
    print(f'#{i} {round(sum/8)}')

testCase = int(input())
values = []
sum = 0
for i in range(0, testCase):
    sum = 0
    tmp = input()
    values = tmp.split()
    values.sort(key=int)
    for j in range(1, 9):
        sum = sum + int(values[j])
    print("#",i+1," ",round(int(sum)/8),sep="")


test_case = int(input())
test_list = []
for i in range(1, test_case + 1):
    result = 0
    tmp = input()
    test_list = tmp.split()
    test_list.sort(key=int)
    for n in test_list[1:9]:
        result += n
    print(f'#{i} {round(result/8)}')