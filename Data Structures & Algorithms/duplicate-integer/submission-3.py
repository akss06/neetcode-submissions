class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        flag = 0
        for num in nums:
            if num not in dict:
                dict[num] = 1
                flag = 0

            else:
                flag = 1
                break

        if flag == 1:
            return True

        else:
            return False
        