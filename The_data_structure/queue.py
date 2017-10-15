#coding:utf-8

"""
队列实现
"""
class Queue(object):
    """implement of Queue."""
    def __init__(self):
        self.__list = []

    def enqueue(self,item):
        """在队列中添加一个item元素"""
        self.__list.append(item)

    def dequeue(self):
        """在队列中删除头部元素"""
        self.__list.pop(0)

    def isEmpty(self):
        """判断队列是否为空"""
        return self.__list == []

    def size(self):
        """返回队列的大小"""
        return len(self.__list)

def main():
    q = Queue()
    print(q.isEmpty())
    q.enqueue(5)
    print(q.size())
if __name__ == "__main__":
    main()
