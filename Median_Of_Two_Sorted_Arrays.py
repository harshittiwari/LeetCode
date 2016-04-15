
class Solution(object):
    def getNext(self, nums1, nums2, ptr1, ptr2):
        if ptr1 == len(nums1):
            x = nums2[ptr2]
            ptr2+=1
        elif ptr2 == len(nums2):
            x = nums1[ptr1] 
            ptr1+=1
        elif nums1[ptr1] < nums2[ptr2]:
            x = nums1[ptr1] 
            ptr1+=1
        else:
            x = nums2[ptr2]
            ptr2+=1
        return ptr1, ptr2, x

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        size = len(nums1) + len(nums2)
        cur = 0
        ptr1 = 0
        ptr2 = 0
        lim = (size // 2) - 1
        while cur < lim:
            if ptr1 == len(nums1):
                ptr2+=1
            elif ptr2 == len(nums2):
                ptr1+=1
            elif nums1[ptr1] < nums2[ptr2]:
                ptr1+=1
            else:
                ptr2+=1
            cur+=1
        if size % 2 == 0:
            x = None
            ptr1, ptr2, x = self.getNext(nums1, nums2, ptr1, ptr2)
            ptr1, ptr2, y = self.getNext(nums1, nums2, ptr1, ptr2)
            return (x + y) / 2
        else:
            ptr1, ptr2, y = self.getNext(nums1, nums2, ptr1, ptr2)
            return y

print(Solution().findMedianSortedArrays([1,2,3,4],[2,4,6,8]))
print(Solution().findMedianSortedArrays([],[2,3]))
print(Solution().findMedianSortedArrays([2,3],[]))