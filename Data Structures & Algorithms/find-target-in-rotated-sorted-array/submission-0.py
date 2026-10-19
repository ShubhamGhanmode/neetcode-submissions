class Solution:
    def search(self, nums: List[int], target: int) -> int:

        i = 0
        j = len(nums) - 1
        mid = nums[i]
        while i <= j:
            # print("Looped")
            if nums[i] < nums[j]:
                # print("Here???",i,nums[i],nums[j])
                mid = min(mid,nums[i])
                break
            m = (i+j)//2
            mid = min(mid,nums[m])

            if nums[m] >= nums[i]:
                i = m + 1
            else:
                j = m-1
        if target <= nums[len(nums)-1]:
            i = nums.index(mid)
            j = len(nums)-1
        elif target:
            i = 0
            j = nums.index(mid)
        
        while i<=j:
            m = (i+j)//2
            if nums[m] < target:
                i = m+1
            elif nums[m] > target:
                j = m-1
            else:
                return m
        return -1