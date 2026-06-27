class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d1 = {}
        l = []

        for num in nums:
            if num not in d1:
                d1[num] = 1

            else:
                d1[num] += 1

        for key,value in d1.items():
            l.append([value,key])

        l.sort(reverse=True)

        
        print(l)    
        l1 = []
        for i in range(k):
            l1.append(l[i][1])

        return l1
        

        

        