class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        for num in nums:
            if num == 0:
                continue
            else:
                product = product * num

        print(product)

        l = []

       

        for i in range(len(nums)):
            if nums[i] == 0:
                l.append(i)

        

        output = []


        for i in range(len(nums)):
            if not l:
                output.append(product//nums[i])

            elif nums[i] != 0 or len(l) > 1:
                output.append(0)

            else:
                output.append(product)

        return output

















