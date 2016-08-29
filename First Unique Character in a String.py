class Solution(object):
    def firstUniqChar1(self, s):
        """
        :type s: str
        :rtype: int
        """
        li = []
        for index in range(len(s)):
            ch = s[index]
            t = -1
            for i in range(len(li)):
                if li[i][0] == ch:
                    t = i
                    break
            if t != -1:
                li[t][1].append(index)
            else:
                li.append([ch,[index]])
        for el in li:
            if len(el[1])==1:
                return el[1][0]
        return -1

    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        li = [0 for _ in range(26)]
        for ch in s:
            li[ord(ch)-97]+=1
        for index in range(len(s)):
            ch = s[index]
            if li[ord(ch)-97] == 1:
                return index
        return -1

sol = Solution()
print(sol.firstUniqChar('leetcode'))
print(sol.firstUniqChar('loveleetcode'))
print(sol.firstUniqChar('aassddwwfwqfq'))