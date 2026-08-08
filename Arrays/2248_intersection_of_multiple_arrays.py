from typing import List

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        set0 = set(nums[0])

        for i in range(1, len(nums)):
            set1 = set0.intersection(set(nums[i]))

        answer = list(set0)
        answer.sort()

        return answer