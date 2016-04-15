class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return 0
        i = 0
        x = abs(dividend)
        y = abs(divisor)
        while x >= y:
            x -= y
            i+=1
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            i = 0 - i
        return i


print(Solution().divide(1,0))
print(Solution().divide(0,1))

print(Solution().divide(0,-3))

print(Solution().divide(4,2))
print(Solution().divide(1,-1))
print(Solution().divide(-1,1))
print(Solution().divide(117,11))