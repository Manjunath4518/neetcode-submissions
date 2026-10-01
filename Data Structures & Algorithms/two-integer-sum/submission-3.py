class Solution:
    def twoSum(self, nums: List[int], x: int) -> List[int]:
        mp = {}

        for i, num in enumerate(nums):
            if x - num in mp:
                return [mp[x - num], i]
            mp[num] = i