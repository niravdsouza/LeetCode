"""
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.
"""
class Solution(object):
    def plusOne(self, digits):
        carry = 1
        for itrn in range(len(digits)-1,-1,-1):
            if digits[itrn] == 9:
                digits[itrn]=0
                carry = 1
            else: 
                digits[itrn]+=1
                carry = 0
                break
        if carry == 1:
            digits.insert(0,1)
        return digits
