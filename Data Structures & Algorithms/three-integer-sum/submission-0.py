class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        r = set()

        for i in range(len(nums)):
            s = set()

            for j in range(i + 1, len(nums)):
                x = -(nums[i] + nums[j])

                if x in s:
                    r.add(tuple(sorted([nums[i], nums[j], x])))

                s.add(nums[j])

        return [list(x) for x in r]