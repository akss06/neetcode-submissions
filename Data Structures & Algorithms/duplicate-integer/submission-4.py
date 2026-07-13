class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        d1 = {}  
        
        for i in range(len(nums)):
            if nums[i] not in d1:
                d1[nums[i]] = i

            else:
                return True

        return False
            

        