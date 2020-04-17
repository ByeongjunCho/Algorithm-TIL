# 5108. [파이썬 S/W 문제해결 기본] 7일차 - 숫자 추가
# Linked List 구현
class Node:
    def __init__(self, data):
        self.data = data
        # self.prev = None  # 이중연결리스트 이전값 포인터
        self.next = None

    # def __del__(self):
    #     print(self.data, '삭제')

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
            self.tail.next = node
            self.tail = node
        self.size += 1

    def insertfirst(self, node):
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    def deletelast(self):
        if self.head is None:
            return

        prev, cur = None, self.head
        while cur.next is not None:
            prev = cur
            cur = cur.next
        prev.next = None
        self.tail = prev

        if prev is None:
            self.head = None
            self.tail = None

        else:
            del cur
            self.size -= 1

    def deletefirst(self):
        if self.head is None:
            return

        cur = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = cur.next

        del cur
        self.size -= 1

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
                node.next = cur
                self.head = node
            elif cur is None:   # 범위를 넘어가는 경우
                cur = node
                self.tail = node
            else:
                node.next = cur
                prev.next = node
        self.size += 1


    def deleteAt(self, idx):
        if self.head is None:
            return
        prev, cur = None, self.head
        j = 0
        while j < idx:
            prev = cur
            cur = cur.next
            j += 1
        if prev is None:
            self.head = self.tail = None
        else:
            prev.next

    def printAt(self, idx):
        if self.head is None:
            return
        else:
            prev, cur = None, self.head
            while idx > 0 and cur is not None:
                prev = cur
                cur = cur.next
                idx -= 1

            if prev is None:
                return cur.data
            else:
                return cur.data
T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())  # 수열의 길이, 추가 횟수, 출력할 인덱스 번호
    tmp = list(map(int, input().split()))
    mylist = List()
    # mylist.head = tmp[0]
    for i in range(0, N):
        mylist.insertlast(Node(tmp[i]))
    for _ in range(M):
        i, j = map(int, input().split())
        mylist.insertAt(i, Node(j))
    print('#{} {}'.format(tc, mylist.printAt(L)))
