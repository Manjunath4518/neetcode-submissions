class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        s = set(nums)
        res = 0
        for i in nums:
            cnt = 1
            if i-1 not in s:
                while i + 1 in s:
                    cnt += 1
                    i = i + 1

            res = max(res,cnt)

        return res