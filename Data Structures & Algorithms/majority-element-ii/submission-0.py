class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        record = {}

        for i in nums:
            if i in record:
                record[i] += 1
            else:
                record[i] = 1
        
        t = len(nums)/3
        output = []

        for i,j in record.items():
            if j > t:
                output.append(i)
        return output