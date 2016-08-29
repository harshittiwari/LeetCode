class Solution(object):
    def findMin(self,nums):
    	if len(nums) == 1:
    		return nums[0]
    	if nums[0] < nums[-1]:
    		return nums[0]
    	mid = len(nums)//2
    	if mid - 1 >= 0 and nums[mid-1] > nums[mid]:
    		return nums[mid]
    	if mid + 1 < len(nums) and nums[mid+1] < nums[mid]:
    		return nums[mid+1]
    	left = self.findMin(nums[:mid])
    	right = self.findMin(nums[mid+1:])
    	if left > right:
    		return right
    	else:
    		return left