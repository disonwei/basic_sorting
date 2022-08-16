"""
插入排序

从第一个元素开始，认为已排序
取下一个元素，对已排序数组从后往前比较 插入
"""

def insertion_sort(alist):

    for i, item_i in enumerate(alist):
        index = i
        while index > 0 and alist[index - 1] > item_i:
            alist[index] = alist[index - 1]
            index -= 1

        alist[index] = item_i

    return alist


unsorted_list = [6, 5, 3, 1, 8, 7, 2, 4]
print(insertion_sort(unsorted_list))