from typing import List

class Solution:
    def addToArrayForm(sel, num: List[int], k: int) -> List[int]:

        carry = 0

        for i in range(len(num) - 1, -1, -1):
            digits_of_k = k % 10
            k = k // 10

            num[i] = num[i] + digits_of_k + carry

            if num[i] >= 10:
                carry = 1
                num[i] = num[i] % 10

            else:
                carry = 0

        while k > 0:
            digit_of_k = k % 10
            k //= 10

            digit = digit_of_k + carry

            if digit >= 10:
                carry = 1
                digit = digit % 10

            else:
                carry = 0

            num.insert(0, digit)

        if carry:
            num.insert(0, carry)

        return num


