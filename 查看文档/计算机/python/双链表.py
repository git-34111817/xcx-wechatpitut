
class Node(object):
    """节点"""
    def __init__(self,item):
        self.next  = None
        self.elem = item
        self.prev = None

class DoubleLinkList(object):
    def __init__(self,node=None):
        self.__head = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head is None

    def length(self):
        """链表长度"""
        cur = self.__head
        # cur游标,用来移动遍历节点
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        while cur is not None:
            print(cur.elem)
            cur = cur.next

    def add(self, item):
        """链表头部添加元素"""
        node = Node(item)
        node.next = self.__head
        self.__head = node
        node.next.prev = node

    def append(self, item):
        """链表尾部添加元素"""
        node = Node(item)
        cur = self.__head
        if self.is_empty():
            self.__head = node
        else:
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, pos, item):
        """指定位置添加元素"""
        if pos <= 0:
            self.add(item)
        elif pos > self.length():
            self.append(item)
        else:
            cur = self.__head
            count = 0
            node = Node(item)
            while count < pos:
                count += 1
                cur = cur.next
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node

    def remove(self, item):
        """删除节点"""
        cur = self.__head
        while cur is not None:
            if cur.elem == item:
                if cur == self.__head:
                    self.__head = cur.next
                    if cur.next:
                        #判断链表是否只有一个节点
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next:
                        cur.next.prev = cur.prev
                    break
            else:
                cur = cur.next

    def search(self, item):
        """查找节点是否存在"""
        cur = self.__head
        while cur is not None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False

#if __name__ == "__main__":
