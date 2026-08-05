class Solution:
    def commonFactors(self, a: int, b: int) -> int:

        count = 0

        # Loop from 1 up to the smaller of the two numbers
        for i in range(1, min(a, b) + 1):
            if a % i == 0 and b % i == 0:
                count += 1

        return count

