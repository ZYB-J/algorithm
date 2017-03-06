"""
@version: 1
@author: zyb
@site: 
@software: PyCharm Community Edition
@file: maxSubarr.py
@time: 2017/3/2 16:20
求一个数组中最大的子数组
"""
import math
def find_max_crossing_subarr(arr,low,mid,high):
    left_sum=0
    i=mid
    sum=0
    max_left=0
    while i>=0:
        sum=sum+arr[i]
        if sum>left_sum:
            left_sum=sum
            max_left=i
        i=i-1

    right_sum=0
    i=mid+1
    sum=0
    max_right=0
    while i<=high:
        sum=sum+arr[i]
        if sum>right_sum:
            right_sum=sum
            max_right=i
        i=i+1

    return (max_left,max_right,left_sum+right_sum)


def find_max_arr(arr,low,high):
    if low==high:
        return (low,high,arr[low])
    else:
        mid=math.floor((low+high)/2)
        (left_low,left_high,left_sum)=find_max_arr(arr,low,mid)
        (right_low,right_high,right_sum)=find_max_arr(arr,mid+1,high)
        (cross_low,cross_high,cross_sum)=find_max_crossing_subarr(arr,low,mid,high)
        if left_sum>=right_sum and left_sum>=cross_sum:
            return (left_low,left_high,left_sum)
        elif right_sum>right_sum and right_sum<cross_sum:
            return (right_low,right_high,right_sum)
        else:
            return (cross_low,cross_high,cross_sum)


if __name__=='__main__':
    arr=[13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
    print(find_max_arr(arr,0,len(arr)-1))

