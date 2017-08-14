"""Max Subarray Incomplete"""
class Solution(object):
    
    def maxSubArray(self, nums):
        self.input=nums
        self.memo=[[-1 for i in range(len(self.input))] for j in range(len(self.input))]
        self.max=nums[0]
        
        op = self.rec(0,len(nums)-1)
        return self.max
        
    def rec(self,start,end):
        
        if end-start==0:
            #print start,self.input[start]
            if self.max< self.input[start]:
                self.max = self.input[start]
            return self.input[start]
        else:
            if self.memo[start][end] is not -1: 
                return self.memo[start][end]
            self.memo[start][end]=max(self.input[start]+self.rec(start+1,end),self.input[end]+self.rec(start,end-1))
            #print start, end, self.memo[start][end]
            if self.max< self.memo[start][end]:
                self.max = self.memo[start][end]
            return self.memo[start][end]
