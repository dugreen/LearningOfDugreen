#coding:utf-8

"""
选择排序实现
"""
import random

def select_sort(alist):
    """选择排序实现"""
    #实现一
    for i in range(len(alist)):
        min = i
        for j in range(len(alist)-i-1):
            if alist[min] > alist[j+i+1]:
                min = j+i+1
        alist[i],alist[min] = alist[min],alist[i]
    #实现二
    # n = len(alist)
    # for i in range(n-1):
    #     min_index = i
    #     for j in range(i,n):
    #         if alist[min_index] > alist[j]:
    #             min_index = j
    #     alist[i],alist[min_index] = alist[min_index],alist[i]


def main():
    alist = []
    for i in range(9):
        alist.append(random.randint(1,100))

    print(alist)
    #alist=[]
    select_sort(alist)
    print(alist)

if __name__ == "__main__":
    main()
