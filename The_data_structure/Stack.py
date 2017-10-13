#coding:utf-8

"""
栈实现
"""

class Stack:
    #初始化栈
    def __init__(self):
        self.items = []

    #压栈操作
    def push(self,item):
        self.items.append(item)
    
    #出栈操作
    def pop(self):
        return self.items.pop()

    #是否为空栈
    def isEmpty(self):
        return (self.items == [])

    #栈的长度
    def size(self):
        return len(self.items)

def main():
    s = Stack()
    s.push(5)
    s.push(4)
    print(s.isEmpty())
    print(s.size())

if __name__ == "__main__":
    main()
