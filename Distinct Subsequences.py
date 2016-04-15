class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if s is None or t is None:
            return 0
        if len(s) == 0 or len(t) == 0:
            return 0
        matrix = [[[] for _ in range(len(s))] for _ in range(len(t))]
        for j in range(len(s)):
            if s[j] == t[0]:
                matrix[0][j] = [1]
        for i in range(1,len(t)):
            found = False
            x = []
            for j in range(len(s)):
                if s[j] == t[i] and found:
                    matrix[i][j] = [y + 1 for y in x]
                if i in matrix[i - 1][j]:
                    found = True
                    x.extend(matrix[i - 1][j])
        ret = 0
        for x in matrix[-1]:
            ret+=len(x)
        return ret

print(Solution().numDistinct("rabbbit","rabbit"))

print(Solution().numDistinct("cadtcdatctacat","cat"))