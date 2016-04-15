class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        high = 0 
        d = {}
        for el in nums:
            if el is None:
                continue
            if el > 0:
                d[el] = el
            if el > high:
                high = el
        if high == 0:
            return 1
        for i in range(1,high+2):
            if i not in d:
                return i
    pass


print(Solution().firstMissingPositive([]))
print(Solution().firstMissingPositive([None]))
print(Solution().firstMissingPositive([1,2,0]))
print(Solution().firstMissingPositive([3,4,-1,1]))