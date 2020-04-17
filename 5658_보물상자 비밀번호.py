# 5658. [모의 SW 역량테스트] 보물상자 비밀번호
from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())  # 4의 배수 / 내림차순 K번째 값
    Q = deque(list(input()))
    passwords = set()
    stop = N // 4
    # 회전
    for _ in range(stop):
        tmp = Q.pop()
        Q.appendleft(tmp)
        for i in range(0, N, stop):
            pwd = ''
            for j in range(i,i+stop):
                pwd +=Q[j]
            passwords.add(pwd)
    sorted_passwords = sorted(list(map(lambda x: int(x, 16), passwords)), reverse=True)
    print("#{} {}".format(tc, sorted_passwords[K-1]))