class Solution(object):
    def findpartition(self,nums,l,h):
        if l == h:
            return l
        if h - l == 1:
            if nums[h] < nums[l]:
                return l
            else: return l - 1
        mid = (l + h) // 2
        if nums[l] < nums[mid]:
            return self.findpartition(nums, mid, h)
        else:
            return self.findpartition(nums,l,mid)

    def binarysearch(self,nums,target,l,h):
        if l == h:
            if l < len(nums) and nums[l] == target: return l
            else: return -1
        m = (l + h) // 2
        if nums[m] == target:
            return m
        elif nums[m] > target:
            return self.binarysearch(nums,target,l,m)
        else:
            return self.binarysearch(nums,target,m + 1,h)

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = [x for x in nums if x is not None]
        if len(nums) == 0:
            return -1
        x = None
        if nums[0] < nums[-1] or len(nums) == 1:
            x = 0
        else:
            x = self.findpartition(nums,0,len(nums) - 1)

        if nums[x] >= target and nums[0] <= target:
            return self.binarysearch(nums,target, 0, x + 1)
        else:
            return self.binarysearch(nums,target,x ,len(nums))
    pass

print(Solution().search([],-1))
print(Solution().search([None],-1))
print(Solution().search([1],0))
print(Solution().search([1,2],0))
print(Solution().search([1,2,3],-1))
print(Solution().search([3,5,1],0))
print(Solution().search([3,5,1],1))
print(Solution().search([3,5,1],5))
print(Solution().search([3,5,1],3))
print(Solution().search([1,2,3,4,5],3))
print(Solution().search([1,2,3,4,5],2))
print(Solution().search([1,2,3,4,5],1))
print(Solution().search([1,2,3,4,5],4))
print(Solution().search([1,2,3,4,5],5))
print(Solution().search([4,5,6,7,8,9,0,1,2],1))
print(Solution().search([4,5,6,7,8,9,0,1,2],6))
print(Solution().search([4,5,6,7,8,9,0,1,2],8))

print(Solution().search([7,8,9,0,1,2,4,5,6],5))
print(Solution().search([7,8,9,0,1,2,4,5,6],8))
print(Solution().search([7,8,9,0,1,2,4,5,6],1))

#-1
#-1
#-1
#-1
#-1
#-1
#2
#1
#0
#2
#1
#0
#3
#4
#7
#2
#4
#7
#1
#4