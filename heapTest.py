"""
@version: 1
@author: zyb
@site: 
@software: PyCharm Community Edition
@file: heapTest.py
@time: 2017/3/13 16:13
"""
"""
n个元素数组
堆排序，初始数据从len//2以后都是叶子节点，叶子节点可以看做是单节点的堆，从后往前，第一个不是叶子节点的节点开始，比较和左右子节点大小，调整
成最大堆（初始数组构建最大堆），循环从1到len-1,交换第一个元素和最后一个元素(最后一个元素已经是最大)，重新调整1到len-2的元素为最大堆
"""
def swap(arr,i,j):
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp

'''
下沉当前i节点，使得当前以i为根节点的树为最大堆
'''
def max_heapify(arr,i,heap_size):
    left=i*2+1
    right=i*2+2
    if left<heap_size and arr[i]<arr[left]:
        largest=left
    else:
        largest=i
    if right<heap_size and arr[right]>arr[largest]:
        largest=right
    if largest!=i:
        swap(arr,largest,i)
        max_heapify(arr,largest,heap_size)


'''
把数组构建最大堆，从最后一个非叶子节点(len/2-1)开始构建最大堆，直到i==0
'''
def build_max_heap(arr,len):
    mid=len//2
    i=mid-1
    heap_size=len
    while i>=0:
        #print(i)
        max_heapify(arr,i,len)
        #print(arr)
        i=i-1


def heap_sorted(arr,len):
    build_max_heap(arr,len)
    remind=len-1
    while remind>=1:
        swap(arr,0,remind)
        max_heapify(arr, 0, remind)
        remind = remind - 1



if __name__=="__main__":
    arr = [ 39, 55, 3, 28, 83, 35,56]
    length=len(arr)
    #build_max_heap(arr,length)
    heap_sorted(arr,length)
    print(arr)