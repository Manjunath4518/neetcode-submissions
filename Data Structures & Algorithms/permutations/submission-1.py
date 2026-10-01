class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations
        return [list(p) for p in permutations(nums)]