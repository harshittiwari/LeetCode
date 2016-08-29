class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        d = {}
        for el in magazine:
            if el in d:
                d[el] += 1
            else:
                d[el] = 1
        for el in ransomNote:
            if el not in d:
                return False
            elif d[el] == 1:
                del d[el]
            else:
                d[el] -= 1
        return True


sol = Solution()
print(sol.canConstruct("a","b"))
print(sol.canConstruct("aa","ab"))
print(sol.canConstruct("aa","aab"))