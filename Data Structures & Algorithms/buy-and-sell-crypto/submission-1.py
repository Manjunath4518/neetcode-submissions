class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        mn = float('inf')

        for i in prices:
            mn = min(mn,i)
            res = max(res,i-mn)

        return res