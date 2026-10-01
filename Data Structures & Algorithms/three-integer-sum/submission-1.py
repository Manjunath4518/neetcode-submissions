class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        for i in range(len(nums)):
            x = -nums[i]
            l = i + 1
            r = len(nums) - 1

            while l < r:
                y = nums[l] + nums[r]

                if y == x:
                    res.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif y < x:
                    l += 1
                else:
                    r -= 1

        return [list(x) for x in res]