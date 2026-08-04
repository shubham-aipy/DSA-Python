from typing import List

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:

        num_set = set(nums)
        missing = []
        min_val = min(nums)
        max_val = max(nums)

        while min_val <= max_val:
            if min_val not in num_set:
                missing.append(min_val)
            min_val = min_val + 1

        return missing