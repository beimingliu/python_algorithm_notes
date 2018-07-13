#source: https://www.bilibili.com/video/av21540971/?p=13


class Node(object):
    """Node"""
    def __init__(self, elem):
        self.elem = elem
        self.next = None

class SingleLinkedList(object):
    """single linked list"""
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """test empty"""
        return self.__head == None

    def length(self):
        """list length"""
        # use cur to traverse
        cur = self.__head
        # count num
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def traverse(self):
        """遍历LinkedList"""
        print("Traversing the LinkedList:")
        cur = self.__head
        while cur != None:
            print(cur.elem, end=" ")
            cur = cur.next
        print("")

    def add(self, item):
        """add node to head, 头插法"""
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        """add node to tail, 尾插法"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        """add in specific location
        :param pos count from 0
        """
        if pos < 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:
            pre = self.__head
            count = 0
            while count < (pos-1):
                count += 1
                pre = pre.next
            # pre points to pos-1
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self, target):
        """remove node given elem"""
        cur  = self.__head
        pre = None
        while cur != None:
            if cur.elem == target:
                # if head node
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, target):
        """check if a node exist"""
        cur = self.__head
        while cur != None:
            if cur.elem == target:
                return True
            else:
                cur = cur.next
        return False

if __name__ == "__main__":
    ll = SingleLinkedList()
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)
    print(ll.is_empty())
    print(ll.length())

    ll.append(2)
    ll.add(8)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    # 8 1 2 3 4 5 6
    ll.insert(-1, 9) # 9 8 123456
    ll.traverse()
    ll.insert(3, 100) # 9 8 1 100 2 3456
    ll.traverse()
    ll.insert(10, 200) # 9 8 1 100 23456 200
    ll.add(5)
    ll.traverse()
    ll.remove(100)
    ll.traverse()
    ll.remove(5)
    ll.traverse()
    ll.remove(200)
    ll.traverse()