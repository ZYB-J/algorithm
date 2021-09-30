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
    print('2222222222266666gg')


def find_max_arr(arr,low,high):
    sum=0
    max_sum=0
    for index,i in enumerate(arr):
        print(index,i)
        sum=sum+arr[index]
        if sum>max_sum:
            max_sum=sum
    return max_sum


if __name__=='__main__':
    arr=[10,1,-4,3,-4]
    find_max_arr(arr,0,4)
    print('-----------------------------')

