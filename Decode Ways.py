class Solution(object):
    def __init__(self):
        self.d = [str(i) for i in range(1,27)]
        self.t = {}

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0:
            return 0
        if s in self.t:
            return self.t[s]
        if len(s) == 1:
            if s in self.d:
                return 1
            else: return 0
        if s[0] == "0":
            return 0
        cnt = 1 * self.numDecodings(s[1:])
        if len(s) > 1 and s[:2] in self.d:
            if len(s) > 2:
                cnt += 1 * self.numDecodings(s[2:])
            else:
                cnt += 1
        self.t[s] = cnt
        return cnt

print(Solution().numDecodings("01"))
print("0")
print("**")
        
print(Solution().numDecodings("12"))
print("2")
print("**")

print(Solution().numDecodings("10"))
print("1")
print("**")

print(Solution().numDecodings("101"))
print("1")
print("**")

print(Solution().numDecodings("110"))
print("1")
print("**")

print(Solution().numDecodings("123"))
print("3")
print("**")

print(Solution().numDecodings("4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948"))