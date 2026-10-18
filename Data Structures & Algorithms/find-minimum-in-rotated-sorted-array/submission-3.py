class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1
        sol = nums[0]
        while i<=j:
            m = (i+j)//2
            # print("i, m, j: ", nums[i],nums[j],nums[m])
            if nums[i] < nums[j]:
                sol = min(sol,nums[i])
                break
            sol = min(sol,nums[m])
            if nums[m] >= nums[i]:
                i = m+1
            
            else:
                j = m-1
        return sol
        

            