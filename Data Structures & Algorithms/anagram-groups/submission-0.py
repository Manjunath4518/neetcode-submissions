class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}

        for s in strs:
            cnt = [0] * 26

            for ch in s:
                cnt[ord(ch) - ord('a')] += 1

            key = tuple(cnt)

            if key not in mp:
                mp[key] = []

            mp[key].append(s)

        return list(mp.values())