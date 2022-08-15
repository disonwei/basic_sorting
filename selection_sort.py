"""
选择排序

找出数组中最小的元素与第一个元素交换位置
剩下的元素中找出最小元素交换位置

"""


# def selection_sort(alist):
#     for i in range(len(alist)):
#         min=alist[i]
#         for j in range(i+1,len(alist)):
#             if alist[j]<min:
#                 min=alist[j]
#         alist[i]=min

#     return alist


def selection_sort(alist):
    for i in range(len(alist)):
        min_index=i
        for j in range(i+1,len(alist)):
            if alist[j]<alist[min_index]:
                min_index=j
        alist[j],alist[min_index]=alist[min_index],alist[j]
    return alist



unsorted_list = [6, 5, 3, 1, 8, 7, 2, 4]
print(selection_sort(unsorted_list))