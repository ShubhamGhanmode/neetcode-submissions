class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        j = 1
        k = len(nums) - 1
        arr = set()
        
        while i < j < k:
            target = -nums[i]
            while j < k:
                if nums[j] + nums[k] < target:
                    j += 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                else:
                    arr.add((nums[i],nums[j],nums[k]))
                    j += 1
                    k -= 1
            i += 1
            j = i+1
            k = len(nums)-1
        return [list(x) for x in arr]



        
        