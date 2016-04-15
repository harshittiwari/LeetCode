import re

class Solution(object):
    def Check(self, s, words, st, l):
        size = len(words[0])
        li = [w for w in words]
        ts = st - size
        tl = l + size
        cond = False
        checked = []
        found = False
        if ts >= 0:
            if s[ts:ts + size] in li:
                found = True
                checked.append(s[ts:ts + size])
                nw = [l for l in li if l != s[ts:ts + size]]
                if len(nw) > 0:
                    x,y = self.Check(s,nw,ts,l)
                    if y < ts: ts = y
                    if x: return True, ts
                else:
                    return True, ts
            else: cond = True
        if tl <= len(s):
            iter = True
            while len(words) - len(checked) > 0 and tl <= len(s) and iter:
                iter = False
                for w in [w for w in words if w not in checked]:
                    if w == s[l:l + size]:
                        checked.append(w)
                        l = l + size
                        iter = True
                        break
            if len(words) == len(checked):
                return True, ts if found else st
        return False, ts if found else st

    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        ret = []
        size = len(words[0])
        for i in [m.start() for m in re.finditer(words[0], s)]:
            if len(words) == 1:
                ret.append(i)
                continue
            x,y = self.Check(s,words[1:],i,i + size)
            if x == True:
                ret.append(y)
            pass
        return ret

x = ['bat', 'bal', 'cat']
y = "batbalcatisbalbatcatiscatbatbalyocatbat"
z = []
print(Solution().findSubstring(y,x))

print(Solution().findSubstring("barfoothefoobarman",["foo","bar"]))
print(Solution().findSubstring("barfoofoobarthefoobarman",["bar","foo","the"]))