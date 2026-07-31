from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        result = []

        for i in range(len(nums)):
            nums[i] = nums[i] ** 2
            result.append(nums[i])

        result.sort(reverse=False)

        return result



