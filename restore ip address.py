class Solution(object):
    def parse(self,s,k):
        key = frozenset([s,k])
        if key in self.d:
            return self.d[key]
        if len(s) < k:
            return []
        if len(s) == k - 1:
            s1 = s[0]
            for i in range(1,len(s)):
                s1 += "." + s[i]
            return [s1]
        li = []
        if k == 0:
            x = int(s)
            if x < 256: return [s]
            else: return[] 
        for i in range(1,min(4,len(s))):
            x = int(s[:i])
            if x < 256:
                for y in self.parse(s[i:],k - 1):
                    li.append(s[:i] + "." + y)
        self.d[key] = li
        return li

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.d = {}
        return self.parse(s,3)

print(Solution().restoreIpAddresses("25525511135"))
print(["255.255.11.135", "255.255.111.35"])
print("**")

print(Solution().restoreIpAddresses("0000"))
print("**")

print(Solution().restoreIpAddresses("000"))
print("**")

print(Solution().restoreIpAddresses("255255255255"))
print("**")

print(Solution().restoreIpAddresses(""))
print("**")

print(Solution().restoreIpAddresses("1604055"))
print("**")