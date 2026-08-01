from typing import List

class Solution:
    def minOperations(self, logs: List[str]) -> int:

        depth = 0

        for log in logs:
            if log == "../": #Move to the parent folder of the current folder(If you are already in the main folder, remain in the same folder)
                depth = max(0, depth - 1)

            elif log == "./": # remain in the same folder
                continue

            else: #move to the child folder(This folder is guaranteed to always exist)
                depth += 1

        return depth