# class Node:
#     def __init__(self, data):
#         self.prev = None
#         self.data = data
#         self.next = None
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def insertLast(self, node):
#         if self.head is None:
#             self.head = self.tail = node
#         else:
#             self.tail.next = node
#             node.prev = self.tail
#             self.tail = node


from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    tmp = deque(map(int, input().split()))
    states = 0
    for _ in range(K):
        states += M
        if states > len(tmp)-1:
            states -= (len(tmp)-1)
        # elif states == len(tmp):
        #     states = len(tmp) - 1
        tmp.insert(states, tmp[states-1] + tmp[states])
        # print(tmp)

    print('#{}'.format(tc), end=' ')
    for i in range(len(tmp)-1, -1, -1):
        if not i or i == len(tmp)-1-9:
            print(tmp[i])
            break
        else:
            print(tmp[i], end=' ')