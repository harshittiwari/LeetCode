#class Solution(object):
#    def fillDict(self, d, s1):
#        for ch in s1:
#            if ch in d:
#                d[ch]+=1
#            else: d[ch] = 1

#    def isInterleave(self, s1, s2, s3):
#        """
#        :type s1: str
#        :type s2: str
#        :type s3: str
#        :rtype: bool
#        """
#        d = {}
#        self.fillDict(d, s1)
#        self.fillDict(d, s2)

#        for ch in s3:
#            if ch not in d:
#                return False
#            d[ch]-=1
#            if d[ch] == 0:
#                del d[ch]
#        return len(d) == 0
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m = len(s1)
        n = len(s2)
        l = len(s3)
        if l != m+n:
            return False
        dp = [[0] * (n+1) for _ in range(m+1)]

        for i in range(0,m+1):
            dp[i][0]  = (s1[:i] == s3[:i])
        for j in range(0,n+1):
            dp[0][j] = (s2[:j] == s3[:j])

        for i in range(1,m+1):
            count = i
            for j in range(1,n+1):
                dp[i][j] = (dp[i-1][j] and (s3[count] == s1[i-1])) or (dp[i][j-1] and (s3[count] == s2[j-1]))
                count += 1
        return dp[m][n]
print(Solution().isInterleave("aabcc","dbbca","aadbbcbcac"))
print(Solution().isInterleave("aabcc","dbbca","aadbbbaccc"))