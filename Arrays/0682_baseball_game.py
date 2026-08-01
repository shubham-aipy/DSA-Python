from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:

        record = [] # for storing score

        for i in range(len(operations)):
            if operations[i] == "+": # when '+' add last 2 scores
                record.append(record[-1] + record[-2])

            elif operations[i] == "D": # when 'D' double the lst score
                record.append(record[-1] * 2)

            elif operations[i] == "C": # when 'C' remove the last score
                record.pop()

            else:
                record.append(int(operations[i]))

        return sum(record) # sum of all scores

