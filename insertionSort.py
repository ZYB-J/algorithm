
def sort(arr:list):
    length = len(arr)
    for i in range(1,length):
        for j in range(i,0,-1):
            if arr[j]<arr[j-1]:
                #print(arr[j],arr[j-1])
                temp = arr[j-1]
                arr[j-1] = arr[j]
                arr[j] = temp


def sort2(arr:list):
    length = len(arr)
    for i in range(1,length):
        key = arr[i]
        j = i-1
        while j>=0 and arr[j]>arr[i]:
            j = j-1

        for k in range(i-1,j,-1):
            print(k,arr[k])
            arr[k+1] = arr[k]
        if j<i-1:
            print(arr)
            arr[j+1] = key

if __name__=="__main__":
    arr = [0,3,4,2,1,5]
    sort2(arr)
    print(arr)
