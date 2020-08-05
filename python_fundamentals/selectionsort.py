arr=[55,69,9,102,4,4,3,99,-1024,256,23,-23,-22,511,200,103,75,-1,-2]

def selectionsort(arr):
#start at arr[0]
#find the minimum of elements arr[1] through arr[last]
#swap min with arr[0]
#start at arr[1]
#find the min in the remaining elements
#swap min with arr[1]
#...n
    last=len(arr)
    min=arr[0]
    for i in range(len(arr)):
        for k in range(i+1,last):
            if arr[k]<arr[i]: #find min of the remaining elements
                min=k
        temp=arr[i]
        arr[i]=arr[min]
        arr[k]=temp
    return(arr)
print(selectionsort(arr))
