

class Node(object):
    """Node"""
    def __int__(self, elem):
        self.elem = elem
        self.next = None

class SingleLinkedList(object):
    """single linked list"""
    def __init__(self, node=None):
        self._head = node

    def is_empty(self):
        """test empty"""
        return self._head == None

    def length(self):
        """list length"""
        pass

    def travel(self):
        """遍历LinkedList"""

    def add(self, item):
        """add node to head """
        pass

    def append(self, item):
        """add node tail """
        pass

    def insert(self, item):
        """add in specific location"""
        pass

    def remove(self, item):
        """remove node """
        pass

    def search(self, item):
        """check if node exist"""
        pass

