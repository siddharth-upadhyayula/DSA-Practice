class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0
        r = 1
        while r<len(prices):
            if prices[l]<prices[r]:
                dif = prices[r]-prices[l]
                if dif>profit:
                    profit = dif
            else:
                l=r
            r+=1
        return profit

#[2,1,4]