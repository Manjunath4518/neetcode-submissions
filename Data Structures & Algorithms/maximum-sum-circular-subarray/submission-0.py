class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        t = sum(nums)

        cm = mx = nums[0]
        cn = mn = nums[0]

        for x in nums[1:]:
            cm = max(x, cm + x)
            mx = max(mx, cm)

            cn = min(x, cn + x)
            mn = min(mn, cn)

        if mx < 0:
            return mx

        return max(mx, t - mn)