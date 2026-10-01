
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mp = Counter(nums)
        return max(mp, key=mp.get)