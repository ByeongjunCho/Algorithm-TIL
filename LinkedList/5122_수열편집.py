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

    def printlistback(self):
        if self.head is None:  # 공백 리스트인지 확인
            return
        cur = self.tail  # 현재 위치의 노드 정보
        print('[ ', end='')
        while cur is not None:
            print(cur.data, end=' ')
            cur = cur.prev
        print(']')

    def insertlast(self, node):
        if self.head is None: # 빈리스트
            self.head = node
            self.tail = node
            
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
                prev.next = node
                node.prev = prev
                node.next = cur
                cur.prev = node

        self.size += 1
    
    def deleteAt(self, idx):
        if self.head == None:
            return
        else:
            cur = self.head
            while idx > 0:
                cur = cur.next
                idx -= 1

            cur.prev.next = cur.next
            cur.next.prev = cur.prev

            del cur
            self.size -= 1
        
    def changeAt(self, tar, dst):
        idxmax = max(tar, dst)
        idxmin = min(tar, dst)
        cur = self.head
        while idxmax > 0:
            cur = cur.next
            if idxmax == idxmin:
                idxmin = cur
            idxmax -= 1
        idxmax = cur
        
        tmp = idxmax
        tmp1 = idxmin
        
        # print(type(idxmin))
        # print(idxmin)
        # print(type(idxmax))
        # print(idxmax)
        idxmin.prev.next = idxmax
        idxmax.prev = tmp1.prev
        idxmax.next = tmp1.next

        idxmax.prev.next = tmp1
        idxmin.prev = tmp.prev
        idxmin.next = tmp.next


            


mylist = List()
for i in range(1, 6):
    mylist.insertlast(Node(i))

mylist.insertAt(2, Node(7))

mylist.deleteAt(2)
mylist.changeAt(1, 4)
mylist.printlist()
mylist.printlistback()




# T = int(input())
# for tc in range(1, T+1):
#     N, M, L = map(int, input().split())
#     Q = deque(map(int, input().split()))
#     for _ in range(M):
#         tmp = input().split()
#         if tmp[0] == 'D':
            