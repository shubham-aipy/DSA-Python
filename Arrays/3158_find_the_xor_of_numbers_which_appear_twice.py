from typing import List
from collections import Counter # Counter used to count how many times a individual integer appears in.

class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:

        counter = Counter(nums)
        result = 0

        for num, freq in counter.items():
            if freq == 2:
                result ^= num

        return result

