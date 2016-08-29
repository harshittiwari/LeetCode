import random
class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type size: int
        """
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        li = [i for i in self.nums]
        random.shuffle(li)
        return li

obj = Solution([i for i in range(10)])
print(obj.reset())
print(obj.shuffle())
print(obj.reset())
print(obj.shuffle())