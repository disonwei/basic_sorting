"""
冒泡排序

持续比较相邻元素，大的挪到后面

"""

from ast import main


def bubbleSort(alist):
    for i in range(len(alist)):
        for j in range(1,len(alist)-i):
            if alist[j-1]>alist[j]:
                alist[j-1],alist[j]=alist[j],alist[j-1]

    return alist


unsorted_list = [6, 5, 3, 1, 8, 7, 2, 4]
print(bubbleSort(unsorted_list))