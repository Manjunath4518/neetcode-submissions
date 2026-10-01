class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]

        for i in range(1,len(nums)):
            pre.append(pre[-1]*nums[i-1])

        suff = [1] * len(nums)

        for i in range(len(nums)-2,-1,-1):
            suff[i] = suff[i+1] * nums[i+1]

        res = [1]*len(nums)
        for i in range(len(nums)):
            res[i] = pre[i] * suff[i]

        return res