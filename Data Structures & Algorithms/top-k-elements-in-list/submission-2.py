class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        # print(d)
        # return [k for k, v in d.items() if v >= k]
        result = sorted(d.keys(), key=lambda x: d[x], reverse=True)
        return result[:k]