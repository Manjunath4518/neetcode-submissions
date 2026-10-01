
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        mp = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []

        if not digits:
            return res

        def solve(pa):
            
            if len(pa) == len(digits):
                res.append(pa)
                return

            
            digit = digits[len(pa)]

            
            for ch in mp[digit]:
                solve(pa + ch)

        solve("")

        return res

