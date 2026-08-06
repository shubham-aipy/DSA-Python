from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        count1 = Counter(nums1)     #Counter makes way easier than running a loop
        count2 = Counter(nums2)

        counts = count1 & count2    #Finds the intersection with its intersection operator (&)

        return list(counts.elements())