"""
快速排序

取基准元素  比基准小排到左边  大排到右边
取 左右两边 重新执行

"""


def quick_sort(alist):
    if len(alist)<=1:
        return alist
    key=alist[0]
    llist,mlist,rlist=[],[],[]
    for i in alist:
        if i<key:
            llist.append(i)
        elif i>key:
            rlist.append(i)
        else:
            mlist.append(i)
    
    return quick_sort(llist)+mlist+quick_sort(rlist)
    


unsorted_list = [6, 5, 3, 1, 8, 7, 2, 4]
print(quick_sort(unsorted_list))


    