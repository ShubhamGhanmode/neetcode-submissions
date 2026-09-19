class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashm = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in hashm:
                return [hashm[diff], i]
            else:
                hashm[n] = i
        