'''
Created on 2016-4-20
堆排序
@author: zhouyongbo
'''
import random

def generateArr(num):
    arr=[]
    for i in range(num):
        arr.append(random.randint(0,100))
    return arr

def swap(arr,i,j):
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp

def sink(arr,k,N):
    while((2*k)<=N):
        j=2*k-1
        if  (j+1)<N and arr[j]<arr[j+1]:
            j+=1
        
        if arr[k-1]>arr[j]:
            break
        swap(arr,k-1,j)
        k=j+1

if __name__=='__main__':
    
    #arr=generateArr(N+1);
    arr=[56, 39, 55, 3, 28, 83, 35, 45, 69, 47, 2, 93, 30, 24,99]
    N=len(arr)
    #arr=[34,56,12]
    print(arr)
    k=N//2
    print(k)
    while k>=1:
        sink(arr, k, N)
        k-=1
    #N=N-1
    while(N>1):
        print(arr)
        swap(arr, 0, N-1)
        N=N-1
        sink(arr, 1, N)
    #swap(arr, 0, N)
    print(arr)
    a=None
    print(a==None)