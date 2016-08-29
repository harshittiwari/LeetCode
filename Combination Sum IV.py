class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #return len(self.combinationSum(nums,target))
        self.d = {}
        return self.combinationSum2(nums,target)

    def combinationSum(self,nums,target):
        li = []
        for i in range(len(nums)):
            num = nums[i]
            if num == target:
                li.append([num])
            elif num < target:
                li2 = self.combinationSum(nums,target-num)
                if len(li2) > 0:
                    for el in li2:
                        el.append(num)
                    li.extend(li2)
                pass
        return li

    def combinationSum2(self,nums,target):
        if target in self.d:
            return self.d[target]
        cnt = 0
        for i in range(len(nums)):
            num = nums[i]
            if num == target:
                cnt += 1
            elif num < target:
                cnt += self.combinationSum2(nums,target-num)
        self.d[target] = cnt
        return cnt
        

sol = Solution()
print(sol.combinationSum4([1,2,3],4))
print(sol.combinationSum4([4,2,1],32))