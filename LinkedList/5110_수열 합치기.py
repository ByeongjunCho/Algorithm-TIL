# from collections import deque
# T = int(input())
#
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     tmp = deque(list(map(int, input().split())))
#     for _ in range(M-1):
#         tmp1 = deque(list(map(int, input().split())))
#         for i in range(len(tmp)):
#             if tmp[i] > tmp1[0]:
#                 for j in range(len(tmp1)):
#                     tmp.insert(i, tmp1[j])
#                     i += 1
#                 break
#         else:
#             tmp.extend(tmp1)
#     print('#{}'.format(tc), end=' ')
#     for i in range(10):
#         if i == 9:
#             print(tmp.pop())
#         else:
#             print(tmp.pop(), end=' ')


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None  # 이중연결리스트 이전값 포인터
        self.next = None

class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def printlist(self):
        if self.head is None:  # 공백 리스트인지 확인
            return
        cur = self.head  # 현재 위치의 노드 정보
        print('[ ', end='')
        while cur is not None:
            print(cur.data, end=' ')
            cur = cur.next
        print(']')


    def insertlast(self, node):
        if self.head is None: # 빈리스트
            self.head = node
            self.tail = node
            return
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1

    def insertAt(self, idx, node): # idx : 삽입 위치, node: 삽입 노드
        if self.head is None:
            self.head = self.tail = node
        else:
            prev, cur = None, self.head
            while idx > 0 and cur is not None:
                prev = cur
                cur = cur.next
                idx -= 1

            if prev is None:  # 데이터가 한개인 경우
                cur.prev = node
                node.next = cur
                self.head = node
                
            elif cur is None:   # 범위를 넘어가는 경우
                cur = node
                cur.prev = prev
                self.tail = node
            else:
                cur.prev = node
                node.next = cur
                prev.next = node

        self.size += 1

    def insertAtAll(self, args):
        cur = self.head
        prev = None

        if cur.data > args[0].data:
            for c in args:
                cur.prev = c
                c.next = cur
                if prev is not None:
                    c.prev = prev
                    prev.next = c
                prev = c
            self.head = args[0]
            return

        while True:
            prev = cur
            cur = cur.next
            if cur is None:
                break
            elif cur.data > args[0].data:
                break
        if cur is None:
            for c in args:
                c.prev = self.tail
                self.tail.next = c
                self.tail = c
        else:
            for c in args:
                c.prev = prev
                c.next = cur
                prev.next = c
                cur.prev = c
                prev = c
    def backprint(self):
        S = []
        tmp = self.tail
        for _ in range(10):
            S.append(str(tmp.data))
            tmp = tmp.prev
        return S


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    tmp = list(map(int, input().split()))
    mylist = List()
    for c in tmp:
        mylist.insertlast(Node(c))
    for _ in range(M-1):
        tmp1 = list(map(int, input().split()))
        S = []
        for cc in tmp1:
            S.append(Node(cc))
        mylist.insertAtAll(S)
    result = mylist.backprint()

    print('#{} {}'.format(tc, ' '.join(result)))
    # print('#{}'.format(tc), end=' ')
    # for i in range(10):
    #     if i == 9:
    #         print(tmp.pop())
    #     else:
    #         print(tmp.pop(), end=' ')
