class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            x = target - nums[i]
            for j in range(i+1,len(nums)):
                if nums[j] == x:
                    return [i+1,j+1]
        pass
    pass

print(Solution().twoSum([2, 7, 11, 15],9))
print(Solution().twoSum([7, 2, 11, 15],9))
print(Solution().twoSum([7, 11, 15, 2],9))