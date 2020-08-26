import unittest

class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        total=num
        for i in nums:
            total+=i
        self.result=total
        return(self)
    def subtract(self, num, *nums):
        # your code here
        pass
# create an instance:
md = MathDojo()
# to test:
x = md.add(2).add(2,5,1).add(3,2).result
print(x)	# should print 5
# run each of the methods a few more times and check the result!


### Add unittest