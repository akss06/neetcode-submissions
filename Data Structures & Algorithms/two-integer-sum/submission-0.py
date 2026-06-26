class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d1 = {}
        

        for i in range(0,len(nums)):
            
            if(target - nums[i] in d1):
                num2 = i
                num1 = d1[target - nums[i]]
                break

            if nums[i] not in d1:
                d1[nums[i]] = i

            
            


            
        
        return [num1,num2]
                

            

        