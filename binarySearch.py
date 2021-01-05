
def binarySearch(arr:list,target:int):
    left = 0
    right = len(arr)-1
    while left<=right:
        mid = (left+right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid]<target:
            left = mid+1
        elif arr[mid]>target:
            right = mid-1
    return -1
if __name__ == "__main__":
    arr = [1,3,4,6,8,12,56,78,99]
    index = binarySearch(arr,5)
    print(arr[index])
