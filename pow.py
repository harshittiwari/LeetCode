class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n in [1,2]:
            return x ** n
        if n % 2 == 0:
            return self.myPow(x ** 2,n // 2)
        else:
            return self.myPow(x ** 2,n // 2) * x

print(Solution().myPow(3,4))

print(Solution().myPow(81,81)==38662196978715633273404758790074316960214213096178319621856934259807530937321861485192508542873470637501160980081794035970219670238407078788135931371782481)