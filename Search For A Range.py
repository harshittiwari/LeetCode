class Solution(object):
    def searchRange(self,nums,target):
    	if len(nums) == 1:
    		if nums[0] == target:
    			return [0,0]
    		else:
    			return [-1,-1]
    	mid = len(nums)//2
    	if nums[mid] < target:
    		if mid + 1 == len(nums):
    			return [-1,-1]
    		li = self.searchRange(nums[mid+1:],target)
    		if li[0] == -1:
    			return li
    		else:
    			return [li[0]+mid+1,li[1]+mid+1]
    	elif nums[mid] > target:
    		return self.searchRange(nums[:mid],target)
    	else:
    		left = mid
    		right = mid
    		if mid + 1 < len(nums) and nums[mid+1] == target:
    			li = self.searchRange(nums[mid+1:],target)
    			right += li[1] + 1
    		if mid - 1 >= 0 and nums[mid-1] == target:
    			li = self.searchRange(nums[:mid],target)
    			left = li[0]
    		return [left,right]