class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}

        for s in strs:
            tup = [0] * 26

            for ch in s:
                tup[ord(ch) - 97] += 1

            tup = tuple(tup)

            if tup in mp:
                mp[tup].append(s)
            else:
                mp[tup] = [s]

        return list(mp.values())