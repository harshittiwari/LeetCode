class Solution(object):
    def threeSum(self,nums,target):
        li = []
        size = len(nums)
        for i in range(size - 2):
            newtarget = target - nums[i]
            if newtarget < nums[i + 1]:
                break
            li2 = []
            for j in range(i + 1,size - 1):
                newtarget2 = newtarget - nums[j]
                if newtarget2 < nums[j + 1]:
                    break
                for k in range(j + 1,size):
                    if nums[k] == newtarget2:
                        li2.append([nums[j] , nums[k]])
            if len(li2) > 0:
                [x.append(nums[i]) for x in li2]
                li.extend(li2)
        return li

    def fourSum(self, nums, target):
        """
        well that escalated quickly
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        size = len(nums)
        ret = []
        for i in range(size - 3):
            li = self.threeSum(nums[i + 1:size],target - nums[i])
            if len(li) > 0:
                [x.append(nums[i]) for x in li]
                ret.extend(li)

        return ret

print(Solution().fourSum([1, 0, -1, 0, -2, 2],0))