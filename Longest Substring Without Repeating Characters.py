class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr = {}
        last = 0
        maxLen = -1
        for i in range(len(s)):
            x = ord(s[i])
            if x not in arr or arr[x] < last:
                arr[x] = i
            else:
                l = i - last
                if l > maxLen:
                    maxLen = l
                last = arr[x] + 1
                arr[x] = i
        
        if len(s) - last > maxLen:
            maxLen = len(s) - last

        return maxLen
    pass

print(Solution().lengthOfLongestSubstring("aabcd"))
print(Solution().lengthOfLongestSubstring("ababca"))
print(Solution().lengthOfLongestSubstring("abcabcdbb"))
print(Solution().lengthOfLongestSubstring("abcabcbb"))
print(Solution().lengthOfLongestSubstring("bbb"))
print(Solution().lengthOfLongestSubstring(""))
print(Solution().lengthOfLongestSubstring("b"))
print(Solution().lengthOfLongestSubstring("acb"))
print(Solution().lengthOfLongestSubstring("dvdf"))
print(Solution().lengthOfLongestSubstring("aab"))