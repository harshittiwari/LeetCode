class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        pointers = []
        sub = ""
        maxLength = -1

        for Index in range(1,len(s)):
            toDeleteIndices = []
            for li in pointers:
                x = li[1] - 1
                if x >= 0 and s[x] == s[Index]:
                    li[1] = x
                    li[0] = Index
                else: toDeleteIndices.append(li)
            for li in toDeleteIndices[::-1]:
                if maxLength < li[0] - li[1] + 1:
                    maxLength = li[0] - li[1] + 1
                    sub = s[li[1]:li[0]+1]
                pointers.remove(li)
            if s[Index] == s[Index - 1]:
                pointers.append([Index, Index - 1])
            if Index - 2 > 0 and s[Index] == s[Index - 2]:
                pointers.append([Index, Index - 2])
        for li in pointers:
            if maxLength < li[0] - li[1] + 1:
                maxLength = li[0] - li[1] + 1
                sub = s[li[1]:li[0]+1]
        if maxLength == -1 and len(s) == 1:
            sub = s
        return sub

        
def longestPalidrome(inputStr):
    pointers = []
    sub = ""
    maxLength = -1

    for Index in range(1,len(inputStr)):
        toDeleteIndices = []
        for li in pointers:
            x = li[1] - 1
            if x >= 0 and inputStr[x] == inputStr[Index]:
                li[1] = x
                li[0] = Index
            else: toDeleteIndices.append(li)
        for li in toDeleteIndices[::-1]:
            if maxLength < li[0] - li[1] + 1:
                maxLength = li[0] - li[1] + 1
                sub = inputStr[li[1]:li[0]+1]
            pointers.remove(li)
        if inputStr[Index] == inputStr[Index - 1]:
            pointers.append([Index, Index - 1])
        if Index - 2 >= 0 and inputStr[Index] == inputStr[Index - 2]:
            pointers.append([Index, Index - 2])
    for li in pointers:
        if maxLength < li[0] - li[1] + 1:
            maxLength = li[0] - li[1] + 1
            sub = inputStr[li[1]:li[0]+1]
    if maxLength == -1 and len(inputStr) == 1:
        sub = inputStr
    return sub

print(longestPalidrome("aaa"))
print(longestPalidrome("abdbbdbc"))
print(longestPalidrome("ecabad"))
print(longestPalidrome("caba"))
print(longestPalidrome("zcabaabazc"))
print(Solution().longestPalindrome("abcbabcbazabcbaaaabcba"))
