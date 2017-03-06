"""
@version: 1
@author: zyb
@site: 
@software: PyCharm Community Edition
@file: test.py
@time: 2017/2/28 11:15
从n个高度的矩形组合成面积最大的矩形，算法的时间复杂度O(n)
"""

def getMax(arr):
    arr.append(0)
    i=0
    size=len(arr)
    stack=[]
    maxsize=arr[0]
    while(i<size):
        if not stack or arr[i]>arr[stack[-1]]:
            stack.append(i)
            i=i+1
        else:
            index=stack.pop()
            if stack:
                width=i-stack[-1]-1
            else:
                width=i
            maxsize=max(maxsize,width*arr[index])
    return maxsize
if __name__=='__main__':
    arr=[2,1,5,6,2,3]
    max = getMax(arr)
    print(max)
