#coding:utf-8

'''
快速排序
Multi-list Quicksort 
'''

def quicksort(L):
    if len(L) <= 1:
        return L
    else:
        pivot = L[len(L)//2]
        
        lower = []
        same = []
        greater = []
        for item in L:
            if item == pivot:
                same.append(item)
            elif item < pivot:
                lower.append(item)
            else:
                greater.append(item)
    return quicksort(lower) + same + quicksort(greater)

def main():
    lis = [4,55,47,23,58,95]
    result = quicksort(lis)
    print(result)
if __name__ == "__main__":
    main()
