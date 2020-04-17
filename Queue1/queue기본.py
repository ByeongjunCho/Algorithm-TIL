N = 10
Q = [0] * N

front, rear = -1, -1

def enqueue(item):
    global rear
    # full 상태 체크
    if front == (rear+1) % N:
        return
    rear = (rear+1) % N
    Q[rear] = item

def dequeue(item):
    global front
    # empty 상태 체크
    if (front+1) % N == rear:
        return
    front = (front+1) % N
    return Q[front]

Q = []
Q.append(1)
while len(Q) > 0:
    Q.pop(0)

from collections import deque
import collections
Q = collections.deque()
Q.extend([1,2,3])
print(Q)
print(Q.popleft())
print(Q)


# 원형 queue
# front, rear = 0, 0
# 삽입 위치 : rear = (rear + 1) mod n
#             front = (front +1) mod n
# full 체크 : if (rear + 1) mod n == front
# empty 체크 : if (front +1) mod n == rear


from heapq import heappush, heappop

Q = []
arr = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]

for val in arr:
    heappush(Q, val)

while len(Q) > 0:
    print(heappop(Q))
print()

# 우선순위큐 + 튜플
from heapq import heappush, heappop

Q = []
arr = [(1, 2), (3,2), (2,3), (2, 5), (3, 1), (2, 2), (4, 4), (4, 2), (4, 1), (1, 1)]

for val in arr:
    heappush(Q, val)
print(type(Q))
while Q:
    print(heappop(Q))
print()

