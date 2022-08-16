"""
归并排序
分治法

将一个列表分为若干个不可再分的小列表
对列表两两合并

"""


from cmath import log


class mergeSort():

    # 分
    def merge(self,A,B):
        l,r=0,0
        sortedArray=[]
        while l<len(A) and r<len(B):
                if A[l]<B[r]:
                    sortedArray.append(A[l])
                    l+=1
                else:
                    sortedArray.append(B[r])
                    r+=1
        
        sortedArray+=A[l:]
        sortedArray+=B[r:]

        print(sortedArray)
        return sortedArray

    # 合
    def merge_sort(self,alist):

        if len(alist)<=1:
            return alist

        min=len(alist)//2

        left=self.merge_sort(alist[:min])
        right=self.merge_sort(alist[min:])

        print(left)
        return self.merge(left,right)



a=mergeSort()  

unsorted_list = [6, 5, 3, 1, 8, 7, 2, 4]
print(a.merge_sort(unsorted_list))

"""
 1 2 3 4
 1 2 3 4 5


"""