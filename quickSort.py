"""
@version: 1
@author: zyb
@site: 
@software: PyCharm Community Edition
@file: quicksort.py
@time: 2017/2/13 11:30
"""
def swap(arr,i,j):
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp
def patition(arr,low,high):
    val=arr[low]
    while(low<high):
        while(low<high and arr[high]>=val):
            high=high-1
        swap(arr, low, high)
        while(low<high and arr[low]<=val):
            low=low+1
        swap(arr,low,high)
    return low

#快速排序的递归实现
def quicksort(arr,a,b):
    if(a>=b):
        return
    p=patition(arr,a,b)
    quicksort(arr,a,p-1)
    quicksort(arr,p+1,b)

class pair(object):
    def __init__(self,left,right):
        self.left=left
        self.right=right


class pair(object):
    def __init__(self, left, right):
        self.left = left
        self.right = right

#快速排序的非递归实现
def noRecur(arr,a,b):
    stack=[]
    stack.append(pair(a,b))
    while stack:
        pr = stack.pop()
        if pr.left>=pr.right :continue
        p=patition(arr,pr.left,pr.right)
        if p<pr.right:
            stack.append(pair(p+1,b))
        else:
            print(p)
        if p>pr.left:
            stack.append(pair(a,p-1))
        else:
            print(p)

if __name__=='__main__':
    arr = [56, 39, 55, 3, 28, 83, 35, 45, 69, 47, 2, 93, 30, 24, 99]
    #arr=[56,39,55,99]
    #swap(arr[0],arr[1]);
    N = len(arr)
    quicksort(arr,0,N-1)
    #noRecur(arr,0,N-1)
    print(arr)