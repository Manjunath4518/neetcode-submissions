class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mx = 0
        cnt = 0

        for i in nums:
            if cnt == 0:
                mx = i

            if i == mx:
                cnt += 1
            else:
                cnt -= 1

        return mx