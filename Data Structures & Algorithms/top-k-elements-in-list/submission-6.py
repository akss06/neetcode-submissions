class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        d = {}

        for i in range(len(nums)):
            
            if not d or nums[i] not in d:
                d[nums[i]] = 1

            else:
                d[nums[i]] += 1

        l = []

        for key,value in d.items():
            l.append([value,key])

        l.sort(reverse = True)

        
        

        l1 = []
        
        for i in range(k):
            l1.append(l[i][1])

        return l1
        

        



        