class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]

        p = nums[0]

        for i in range(1,len(nums)):
            pre.append(p)
            p *= nums[i]

        s = nums[-1]

        for i in range(len(nums)-2,-1,-1):
            pre[i] *= s
            s *= nums[i]
        
        return pre