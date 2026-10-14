class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def solve(x):
            cnt = 0
            for i in piles:
                cnt += math.ceil(i / x)
            return cnt <= h

        l, r = 1, max(piles)

        while l < r:
            mid = (l + r) // 2

            if solve(mid):
                r = mid
            else:
                l = mid + 1

        return l
        