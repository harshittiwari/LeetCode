import re
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        last = 0
        for ch in s:
            if ch != " ":
                l+=1
            else:
                if l > 0:
                    last = l
                    l = 0
        if l > 0:
            last = l
        return last

        if len(s) == 0:
            return 0
        li = [m.start() for m in re.finditer("\s+", s)]
        if len(li) == 0:
            return len(s)
        x = -1
        while abs(x) != len(s):
            if len(s) - li[-1] - 1 != 0:
                return len(s) - li[-1] - 1
            abs-=1
        return len(s) - li[-1] - 1

print(Solution().lengthOfLastWord("a "))
print(Solution().lengthOfLastWord("a"))
print(Solution().lengthOfLastWord("b   a    "))