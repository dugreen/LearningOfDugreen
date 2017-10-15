#coding:utf-8

'''
In-place Quicksort 
'''
def partition(data, first, last): # first & last specify a slice data list to work on
    pivot = data[first] # choose leftmost element as the pivot
    left, right = first + 1, last
    while left <= right:
        while left < right and data[left] < pivot: # Find first key > pivot
            left += 1
        while right >= left and data[right] >= pivot: # Find rightmost key < the pivot
            right -= 1
        if left < right: # Need to exchange left/right?
            data[left], data[right] = data[right], data[left]
        elif left == right: # if left-right meet, we've finished
            break
    
    if right != first: # finally, put pivot element in place
        data[first], data[right] = data[right], data[first]
    
    return right # return the index of pivot 19

def quicksort(list,bottom,top):
    if bottom < top:
        split = partition(list,bottom,top)

        quicksort(list,bottom,split-1)
        quicksort(list,split+1,top)
    else:
        return

def main():
    lis = [47,58,24,16,95,2]
    quicksort(lis,0,len(lis)-1)
    print(lis)

if __name__ == "__main__":
    main()

