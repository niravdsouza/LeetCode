"""Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""
class Solution(object):
    def singleNumber(self, nums):
        numbers={}
        for num in nums:
            if num not in numbers:
                numbers[num]=1
            else:
                del(numbers[num])
        return numbers.keys()[0]
        
