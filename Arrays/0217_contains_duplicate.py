from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        seen = set()

        for num in nums:
            if num in seen:
                return True  #return true when any value appears at least twice in the array
            else:
                 seen.add(num)

        return False #return false if every element is distinct
