class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        i = 0
        res = []
        while i<min(len(strs[0]),len(strs[-1])):
            if strs[0][i] == strs[-1][i]:
                res.append(strs[0][i])
                i += 1
            else:
                break

        return ''.join(res)