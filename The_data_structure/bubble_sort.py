#coding:utf-8

import random

"""
冒泡排序实现
"""
def bubble_sort(alist):
    """冒泡排序"""
    for i in range(len(alist)):
        for j in range(len(alist)-i-1):
            if alist[j] > alist[j+1]:
                alist[j],alist[j+1] = alist[j+1],alist[j]


def main():
    alist = []
    for i in range(9):
        alist.append(random.randint(1,100))

    print(alist)
    #alist=[]
    bubble_sort(alist)
    print(alist)

if __name__ == "__main__":
    main()
