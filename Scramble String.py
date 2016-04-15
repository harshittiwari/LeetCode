import math
class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) != len(s2): return False
        if s1 == s2: 
            return True
        if len(s1) <= 2:
            if s1 != s2[::-1]: 
                return False
            else: 
                return True
        if sorted(s1) != sorted(s2):
            return False

        mid = len(s1) // 2
        for i in range(1,len(s1)):
            x = self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:],s2[i:])
            y = self.isScramble(s1[:i],s2[-i:]) and self.isScramble(s1[i:],s2[:-i])
            if x or y: return True
        return False

print(Solution().isScramble("abc","cab"))
print(Solution().isScramble("great","rgtae"))
print(Solution().isScramble("great","taerg"))
print(Solution().isScramble("abb","bab"))
print(Solution().isScramble("abc","bac"))
