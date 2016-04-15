from math import ceil 
class Solution(object):
    def calculate(self, cn, i, matrix, n, num1, num2, x,digits):
        ndigits = -1 * digits
        y = cn - 1
        for j in range(n - 1,0,ndigits):
            if i + ndigits + 1 >= 0 and j + ndigits + 1 >= 0:
                matrix[x][y] = int(num1[i + ndigits + 1:i + 1]) * int(num2[j + ndigits + 1:j + 1])
            if i + ndigits + 1 < 0 and j + ndigits + 1 >= 0:
                matrix[x][y] = int(num1[:i + 1]) * int(num2[j + ndigits + 1:j + 1])
            elif i + ndigits + 1 >= 0 and j + ndigits + 1 < 0:
                matrix[x][y] = int(num1[i + ndigits + 1:i + 1]) * int(num2[:j + 1])
            else:
                matrix[x][y] = int(num1[:i + 1]) * int(num2[:j + 1])
            y -=1
        if n - 1 == 0:
            if i + ndigits + 1 < 0:
                matrix[x][y] = int(num1[:i + 1]) * int(num2)
            else:
                matrix[x][y] = int(num1[i + ndigits + 1:i + 1]) * int(num2)
        x-=1
        return x

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        digits = 5
        if int(num1) == 0 or int(num2) == 0:
            return "0"

        m = len(num1)
        n = len(num2)
        cm = int(ceil(m / digits))
        cn = int(ceil(n / digits))

        matrix = [[0 for x in range(cn)] for y in range(cm)]

        x = cm - 1
        for i in range(m - 1,0,-1 * digits):
            x = self.calculate(cn, i, matrix, n, num1, num2, x,digits)
        if m - 1 == 0:
            self.calculate(cn, 0, matrix, n, num1, num2, x,digits)
        
        ret = ""

        sum = cm + cn - 2
        carry = 0
        for s in range(sum,-1,-1):
            x = carry
            for j in range(cn):
                for i in range(cm):
                    if i + j == s:
                        x+=matrix[i][j]
            if x // 1000 > 0:
                ret = str(x)[-1 * digits:] + ret
                carry = x // (10 ** digits)
            else:
                carry = 0
                ret = str(x) + ret
        if carry > 0:
            ret = str(carry) + ret

        #print(matrix)
        return ret

print(Solution().multiply("123456","456123"))
print(Solution().multiply("23456","456123"))
print(Solution().multiply("23456","4"))
print(Solution().multiply("2","12344"))
print(Solution().multiply("1","2"))
print(Solution().multiply("1","1"))
print(Solution().multiply("0","0"))

print(Solution().multiply("0","456123"))
print(Solution().multiply("23456","0"))