class Solution(object):
    def FindNearest(self,num,t):
        x = t * 10
        min = num
        ind = 0
        for i in range(1,10):
            y = num - (x + i) * i
            if y >= 0 and y < min:
                min = y
                ind = i
        return ind

    def mySqrt(self, num):
        """
        :type x: int
        :rtype: int
        """
        s = str(num)
        st = 0
        e = 1
        if len(s) % 2 == 0:
            e = 2
        num = 0
        t = 0
        sqrt = 0
        while e < len(s) + 1:
            num = (num * 100) + int(s[st:e])

            x = self.FindNearest(num,t)
            num = num - (((t * 10) + x) * x)
            t = (t * 10) + (x * 2)
            sqrt = (sqrt * 10) + x
            
            st,e = e,e+2
            

        return sqrt

print(Solution().mySqrt(9025))
print(Solution().mySqrt(625))
print(Solution().mySqrt(10816))
print(Solution().mySqrt(9))
print(Solution().mySqrt(64))