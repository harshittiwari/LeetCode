class Solution(object):
    def permuteUnique(self, li):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        li = [x for x in li if x is not None]
        if len(li) == 1:
            return [li]
        ret = []
        done = []
        for i in range(len(li)):
            x = li[i]
            if x in done:
                continue
            done.append(x)
            t = self.permuteUnique(li[:i]+li[i+1:])
            for y in t:
                y.insert(0,x)
            ret.extend(t)
        return ret

print(Solution().permuteUnique([1,2,3]))
print(Solution().permuteUnique([1,1,3]))
print(Solution().permuteUnique([1,1,1]))
print(Solution().permuteUnique([None]))
print(Solution().permuteUnique([]))
print(Solution().permuteUnique([3,3,0,0,2,3,2]))