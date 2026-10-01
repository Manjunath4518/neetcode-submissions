class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        tup = list(count.items())

        tup.sort(key=lambda x: x[1], reverse=True)

        return [x[0] for x in tup[:k]]