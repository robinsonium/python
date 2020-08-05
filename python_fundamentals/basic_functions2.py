#Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
#Example: countdown(5) should return [5,4,3,2,1,0]
def countdown(num):
    mylist=[]
    for i in range(num,-1,-1):
        mylist.append(i)
    return(mylist)
foo=countdown(9)
print(foo)

#version 2
def countdown2(num):
    mylist=list(range(num,-1,-1))
    return(mylist)
bar=countdown2(20)
print(bar)

#Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
#Example: print_and_return([1,2]) should print 1 and return 2
def print_and_return(mylist):
    print(mylist[0])
    return(mylist[1])
#test
x=print_and_return([1,2])
print("x=",x)

#First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
#Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)
def first_plus_length(mylist):
    length=len(mylist)
    return(length+mylist[0]) 
#test case, should output '11'
print(first_plus_length([6,10,23,1,17]))
print("Done with first_plus_length")
#Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
#Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
#Example: values_greater_than_second([3]) should return False
def greater_than_second(mylist):
    newlist=[]
    second=mylist[1]
    count=0
    for i in range(0,len(mylist)-1):
        if mylist[i]>second:
            newlist.append(mylist[i])
            count+=1
    print(count)
    return(newlist)
#test case
foo=greater_than_second([2,16,4,2,99,107,25,15])
print(foo)
print("done with greater_than_second")

#This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
#Example: length_and_value(4,7) should return [7,7,7,7]
#Example: length_and_value(6,2) should return [2,2,2,2,2,2]
def this_length_that_value(size,value):
    newlist=[]
    for value in size:
        newlist.append(value)
    return(newlist)
#test case
print(this_length_that_value(4,7))
print(this_length_that_value(6,2))


