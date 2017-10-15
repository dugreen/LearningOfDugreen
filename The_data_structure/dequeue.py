#coding:utf-8

"""
双向队列实现
"""

class Deque(object):
    """implement for Deque."""
    def __init__(self):
        self.__list = []
        #self.list = []
    def add_front(self, item):
        """往队列前部添加一个item元素"""
        self.__list.insert(0, item)

    def add_rear(self, item):
        """往队列后部添加一个item元素"""
        self.__list.append(item)

    def pop_front(self):
        """从队列头部删除一个元素"""
        return self.__list.pop(0)

    def pop_rear(self):
        """从队列尾部删除一个元素"""
        return self.__list.pop()

    def isEmpty(self):
        """判断队列是否为空"""
        return self.__list == []

    def size(self):
        """队列的大小"""
        return len(self.__list)


def main():
    d = Deque()
    d.add_front(7)
    d.add_rear(5)
    d.add_rear(4)
if __name__ == "__main__":
    main()
