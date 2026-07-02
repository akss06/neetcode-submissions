class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        maxi = 0
        

        while left < right:
            level = (right - left) * min(heights[right],heights[left])
            
            maxi = max(maxi,level)

            if heights[left] < heights[right]:
                left += 1

            elif heights[left] > heights[right]:
                right -= 1

            else:
                left += 1

        return maxi

        
                

        
        