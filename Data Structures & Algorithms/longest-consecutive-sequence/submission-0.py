class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_sorted = list(sorted(set(nums)))
        
        
        current = 1
        longest = 1
        i = 0
        while i < len(nums_sorted)-1:
            if nums_sorted[i+1] != nums_sorted[i] + 1:
                i = i + 1

                if current > longest:
                    longest = current
                current = 1

            else:
                current += 1
                longest = max(current,longest)
                i = i + 1


        return longest
        


            
        