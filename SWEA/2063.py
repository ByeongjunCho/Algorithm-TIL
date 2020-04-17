num = int(input())
case = list(map(int, input().split(' ')))

print(sorted(case)[int(len(case)/2)])