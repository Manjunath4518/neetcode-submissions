class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mp = Counter(nums)
        for i in mp:
            if mp[i] > 1:
                return True

        return False