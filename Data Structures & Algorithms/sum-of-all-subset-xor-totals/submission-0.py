class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def f(i, x):
            if i == len(nums):
                return x

            return f(i + 1, x ^ nums[i]) + f(i + 1, x)

        return f(0, 0)