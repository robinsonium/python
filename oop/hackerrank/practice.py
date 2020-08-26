# simple array sum
# Given an array of integers, find the sum of its elements.
def sumArray(arr):
    total=0
    for i in range(len(arr)):
        total+=arr[i]
    return total

