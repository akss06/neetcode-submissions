class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = [ [] for _ in range(len(nums) + 1)]

        d = {}

        for i in range(len(nums)):
            
            if not d or nums[i] not in d:
                d[nums[i]] = 1

            else:
                d[nums[i]] += 1

        
        for key,value in d.items():
            l[value].append(key)


        res = []

        for i in range(len(l) - 1,0,-1):
            for num in l[i]:
                res.append(num)

            if len(res) == k:
                return res

        

        

        


        
            

        