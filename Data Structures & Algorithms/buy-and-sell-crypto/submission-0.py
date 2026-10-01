class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn = prices[0]
        res = 0

        for i in prices:
            res = max(res,i - mn)
            mn = min(mn,i)

        return res