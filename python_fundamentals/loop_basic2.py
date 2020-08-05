# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
def biggie_size(mylist):
    for i in range(len(mylist)):
        if mylist[i]>0:
            mylist[i]="big"
    return mylist
#test case
print(biggie_size([-1, 3, 5, -5]))
print("Done with biggie size")

# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
def count_positives(mylist):
    count=0
    for i in range(len(mylist)):
        if mylist[i]>0:
            count+=1
    mylist[len(mylist)-1]=count
    return(mylist)
#test case
print(count_positives([-1,1,1,1]))
print(count_positives([1,6,-4,-2,-7,-2]))
print("done with count_positives")

#Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7
def sum_total(mylist):
    total=0
    for i in range(len(mylist)):
        total=total+mylist[i]
    return(total)
#test case
print(sum_total([1,2,3,4]))
print(sum_total([6,3,-2]))
print("Done with sum_total()")

#Average - Create a function that takes a list and returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5
def ave(mylist):
    count=len(mylist)
    total=0
    for i in range(len(mylist)):
        total=total+mylist[i]
    average=total/count
    return(average)
#test case
print(ave([1,2,3,4]))# should return 2.5
print("done with ave()")

#Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0
def length(mylist):
    # assuming we aren't supposed to use len() here
    count=0
    for i in mylist:
        count+=1
    return(count)
#test case
print(length([37,2,1,-9]))# should return 4
print(length([]))# should return 0
print("done with length()")

#Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False
def minimum(mylist):
    if len(mylist)==0:
        return False
    else:
        val=mylist[0]# We'll assume the first element is the minimum, and correct it if needed as we go through the list
        for i in range(len(mylist)):
            if mylist[i]<val:
                val=mylist[i]
    return val
#test case
print(minimum([37,2,1,-9]))
print(minimum([1,2,3,4]))
print(minimum([]))
print("Done with minimum()")

#Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False
def maximum(mylist):
    if len(mylist)==0:
        return False
    else:
        val=mylist[0]# We'll assume the first element is the maximum, and correct it if needed as we go through the list
        for i in range(len(mylist)):
            if mylist[i]>val:
                val=mylist[i]
    return val
#test case
print(maximum([37,2,1,-9]))
print(maximum([1,2,3,4]))
print(maximum([]))
print("Done with maximum()")

#Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
def ultimate_analysis(mylist):
    length=0
    minimum=mylist[0]
    maximum=mylist[0]
    sumtotal=0
    for i in mylist:
        length+=1 # Here we get our list length for use in the rest of the routine
    for i in range(length):
        if mylist[i]<minimum:
            minimum=mylist[i]
        elif mylist[i]>maximum:
            maximum=mylist[i]
        sumtotal=sumtotal+mylist[i]
    average=sumtotal/length
    return {'sumtotal':sumtotal,'average':average,'minimum':minimum,'maximum':maximum,'length':length}
#test case
print(ultimate_analysis([37,2,1,-9]))
print("done with ultimate analysis")

#Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
def reverse_list(mylist):
    lastindex=len(mylist)-1
    for i in range(int(lastindex/2)):
        temp=mylist[i]
        mylist[i]=mylist[lastindex-i]
        mylist[lastindex-i]=temp
    return mylist
#test case
print(reverse_list([37,2,1,-9]))
print(reverse_list([11,10,9,8,7,6,5,4,3,2,1]))
print("done with reverse_list()")