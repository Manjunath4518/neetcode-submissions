class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = j = 0
        ans = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                ans.append(nums1[i])
                i += 1
            else:
                ans.append(nums2[j])
                j += 1

        ans.extend(nums1[i:])
        ans.extend(nums2[j:])

        n = len(ans)

        if n % 2:
            return ans[n // 2]
        else:
            return (ans[n // 2 - 1] + ans[n // 2]) / 2