class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        pre_product = 1
        post_product = 1

        for i in range(len(nums)):
            output.append(1)
            
        for i in range(1,len(nums)):
            pre_product *= nums[i-1]
            output[i] = pre_product

        for i in range(len(nums) - 1,-1,-1):
            
            output[i] *= post_product
            post_product *= nums[i]


        return output


        