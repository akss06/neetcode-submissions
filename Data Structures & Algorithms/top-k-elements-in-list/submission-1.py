class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d1 = {}

        for i in nums:
            if i not in d1:
                d1[i] = nums.count(i)

            else:
                continue

        print(d1)
        
        sorted_d = sorted(d1, key=d1.get, reverse=True)
        

        return sorted_d[0:k]


        
        
        


        
        