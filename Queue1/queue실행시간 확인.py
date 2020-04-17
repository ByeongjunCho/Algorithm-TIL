#python3
#import atexit
from queue import Queue
from collections import deque
from time import time, strftime, localtime
from datetime import timedelta
SIZE = 300000
class myQ:
    def __init__(self, size):
        self.arr = [0] * size
        self.front = -1
        self.rear = -1

    def push(self, item):
        self.rear += 1
        self.arr[self.rear] = item

    def pop(self):
        self.front += 1
        return self.arr[self.front]

    def empty(self):
        return self.front == self.rear

start = 0

def log(s):
    global start
    start = time()
    print('시작 >>>> ', s)

def endlog():
    line = "=" * 40
    elapsed = time() - start
    print("실행 시간: ", elapsed)
    print('종료 >>>> ')
    print(line)

log("List 사용")
Q = []
for i in range(SIZE):
    Q.append(i)

while len(Q) > 0:
    Q.pop(0)
endlog()

log("queue.Queue 사용")
Q = Queue()
for i in range(SIZE):
    Q.put(i)

while not Q.empty():
    Q.get()
endlog()

log("collections.deque 사용")
Q = deque()
for i in range(SIZE):
    Q.append(i)

while len(Q) > 0:
    Q.popleft()
endlog()

log("List 인덱싱")
Q = myQ(SIZE)
for i in range(SIZE):
    Q.push(i)

while not Q.empty():
    Q.pop()
endlog()
