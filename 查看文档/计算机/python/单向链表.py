# coding utf-8
#cur指的是指向指针
#pre指的是指向指针
#item指的存放的数据
#pos指的是位置 往往和item合并做参数传递title


class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None

class SingleLinkList(object):

    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head is None

    def length(self):
        """链表长度"""
        cur = self.__head
        #cur游标,用来移动遍历节点
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

    def insert(self, pos, item):
        """指定位置添加元素"""
        if pos<= 0:
            self.add(item)
        elif pos > self.length():
            self.append(item)
        else:
            pre = self.__head
            count = 0
            node = Node(item)
            while count < (pos-1):
                count += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node


    def remove(self,item):
        """删除节点"""
        cur = self.__head
        pre = None
        while cur is not None:
            if cur.elem == item:
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                    break
            else:
                pre =cur
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

if __name__ == "__main__":
    li = SingleLinkList()
    print(li.is_empty())
    print(li.length())

    li.add(5)
    print(li.is_empty())
    print(li.length())

    li.append(2)
    li.append(3)
    li.append(4)
    li.append(5)
    li.append(6)
    li.add(5)
    li.append(7)
    li.insert(2,1000)
    li.travel()
