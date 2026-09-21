class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = len(nums)
        dict1 = {}
        freq = [[] for i in range(l +1)]
        items = []
        # print(freq)

        for i in nums:
            dict1[i] = 1 + dict1.get(i,0)
        # print(dict1.items())
        for n,c in dict1.items():
            freq[c].append(n)
        # print(freq)
        for i in range(l,0,-1):
            if freq[i] != []:
                items += freq[i]
            if len(items) == k:
                return items