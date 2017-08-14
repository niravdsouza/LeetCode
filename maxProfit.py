"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
"""


class Solution(object):

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<=1:
            return 0
        maxi = prices[0]
        mini = prices[0]
        maxa = 0
        mina = 0
        alldecreasing=True
        for i in range(1,len(prices)):
            if prices[i]>maxi:
                #print "Max is",prices[i]," at ",i
                maxi=prices[i]
                maxa=i
                if i == 1:
                    alldecreasing=False
                if i > 1 and alldecreasing==True:
                    #print "In Here"
                    return self.maxProfit(prices[mina:])
            elif prices[i]<=mini:
                #print "Min is",prices[i]," at ",i
                mini=prices[i]
                mina=i
            else:
                if alldecreasing==True:
                    alldecreasing=False
                    return self.maxProfit(prices[i-1:])
                
        #print mina,maxa
        if mina<maxa:
            #print maxi-mini
            return maxi-mini
        elif mina==maxa:
            return 0
        else:
            if alldecreasing==True:
                return 0
            return max(self.maxProfit(prices[0:maxa+1]),self.maxProfit(prices[maxa+1:mina]),self.maxProfit(prices[mina:]),0)
