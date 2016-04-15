class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        ret = ""
        for i in range(numRows):
            rem = numRows - i - 1
            if i % 2 == 0:
                ret = ret + s[i::numRows + numRows // 2]
            else:
                t = rem + i // 2 + 1
                inc = t
                j = i
                while j < len(s):
                    ret = ret + s[j]
                    j += inc
                    if inc == t:
                        inc = rem // 2 + i + 1
                    else:
                        inc = t
        return ret

print(Solution().convert("paypalishiring",3))
print(Solution().convert("paypalishiringtodayk",7))
print(Solution().convert("paypalishiring",5))