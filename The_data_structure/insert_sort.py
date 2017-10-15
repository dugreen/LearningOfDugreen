#coding:utf-8

"""
插入排序实现
"""
import random

def insert_sort(alist):
    n = len(alist)
    for i in range(1,n):
        while i > 0:
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]
                i -= 1
            else:
                break
def main():
    alist = []
    for i in range(9):
        alist.append(random.randint(1,99))

    print(alist)
    insert_sort(alist)
    print(alist)

if __name__ == "__main__":
    main()
