class Solution(object):
    def permute(self, li):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        li = [x for x in li if x is not None]
        if len(li) == 1:
            return [li]
        ret = []
        for i in range(len(li)):
            x = li[i]
            t = self.permute(li[:i]+li[i+1:])
            for y in t:
                y.insert(0,x)
            ret.extend(t)
        return ret

print(Solution().permute([1,2,3]))
print(Solution().permute([None]))
print(Solution().permute([]))