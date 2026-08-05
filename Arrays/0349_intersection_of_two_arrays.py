from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        nums1 = sorted(nums1)
        nums2 = sorted(nums2)

        result = list(set(nums1) & set(nums2)) #this extracts the intersection from both arrays

        return result