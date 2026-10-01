class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False


        c = [0] * 26

        for a,b in zip(s,t):
            c[ord(a) - 97] += 1
            c[ord(b) - 97] -= 1

        return all(x==0 for x in c)
        