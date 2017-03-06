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
    print('22222222222')


def find_max_arr(arr,low,high):
    sum=0
    max_sum=0
    for i in arr:
        sum=sum+arr[i]
        if sum>max_sum:
            max_sum=sum


if __name__=='__main__':
    arr=[10,1,-4,3,-4]
    find_max_arr(arr,0,4)

