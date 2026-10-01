class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        mx = 0

        for i in s:
            if i - 1 not in s:
                c = 1
                j = i

                while j + 1 in s:
                    j += 1
                    c += 1

                mx = max(mx, c)

        return mx