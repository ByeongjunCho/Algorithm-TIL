# file에서 문자열 불러오기
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
arr = list(map(int, input().split()))

print(N, arr)