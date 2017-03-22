"""
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.
"""
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        temp=1
        for i in range(len(digits)-1,-1,-1):
            print i
            digits[i]+=temp
            temp=0
            if digits[i]==10:
                digits[i]=0
                temp=1
        if temp==1:
            digits=[1]+digits
        return digits
