#coding:utf-8

"""
迭代器练习
"""

#导入随机数模块
import random

#创建可操作的迭代类
class Bag():
    #初始化可迭代对象
    def __init__(self, itemList):
        self.items = itemList
    
    #当前对象长度
    def __len__(self):
        return len(self.items)

    #显示对象内容
    def display(self, title = ""):
        print(title, self.items)

    
    def __repr__(self):
        return "\n".join(self.items)

    # Now make this object support an iterator
    def __iter__(self):
        self.index = 0
        random.shuffle(self.items)
        return self

    def __next__(self):
        if self.index < len(self.items):
            result = self.items[self.index]
            self.index +=1
            return result
        else:
            raise StopIteration

def examinClass():
    myToys = Bag( ["apple",  "bear", "blue cup", "red car",] )
    myLunch = Bag(["drink", "rice", "vegetables"])

    myToys.display()

    # Test that __len__() allows len() to work
    print("\n>>> Lunch")
    print("len(myLunch) is", len(myLunch))

    # Test that the iterator works
    print("Lunch")
    for x in (myLunch):
        print(x)

    print(">>> Toys")
    for item in myToys:
        print(item)
    # Test that the iterator allows 'in' to work
    if "bear" in myToys:
        print("I like bears")

    if "doll" in myToys:
        print("and dolls")
    else:
        print("No dolls")



if __name__ == '__main__':
    examinClass()
