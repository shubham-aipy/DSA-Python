from typing import List

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        min_com_int = set(nums1)

        for num in nums2:
            if num in min_com_int:
                return num

        return -1
