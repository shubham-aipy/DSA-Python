from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        triangle = []

        for i in range(numRows):
            row = []

            if i == 0:
                row.append(1)

            else:
                prev = triangle[i - 1]

                row.append(1)

                for j in range(len(prev) - 1):
                    mid = prev[j] + prev[j + 1]
                    row.append(mid)

                row.append(1)

            triangle.append(row)

        return triangle




