arr=[55,69,9,102,4,4,3,99,-1024,256,23,-23,-22,511,200,103,75,-1,-2]

def bubblesort(arr):
    count=len(arr)
    swaps=0
    while count>=0:
        for i in range(len(arr)-1):
            first=arr[i]
            second=arr[i+1]
            print(f"comparing {first} and {second}")
            if first>second:
                arr[i],arr[i+1] = arr[i+1],arr[i]
                print(f"swapping {first} and {second}")
                swaps+=1
        count=count-1
    print(f"Made {swaps} swaps")
    return arr

# test case
print(bubblesort(arr))