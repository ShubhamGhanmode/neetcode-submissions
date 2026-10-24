class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        right = []
        l = 1
        r = 1
        for i in range(len(nums)):
            neg = -(i+1)

            l = l*nums[i]
            r = r*nums[neg]

            left.append(l)
            right.append(r)
        left.pop()
        left.insert(0,1)
        right.pop()
        right.insert(0,1)
        output = []
        # print("Left",left)
        # print("right",right)
        for i in range(len(nums)):
            # print("l,r:",left[i],right[-(i+1)])
            output.append(left[i]*right[-(i+1)])
        return output